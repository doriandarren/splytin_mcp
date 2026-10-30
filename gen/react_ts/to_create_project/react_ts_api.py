

import os
from gen.helpers.helper_file import HelperFile


class ReactTsApi:

    def invoke(self, full_path):
        self.create_api_error_ts(full_path)
        self.create_api_ts(full_path)
        self.create_json_api_types_ts(full_path)
        
        
        
    
    def create_api_error_ts(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "api")
    
        content = r'''// src/api/api-error.ts
import type { JsonApiError } from './json-api.types';

type ApiErrorKind = 'http' | 'network' | 'timeout' | 'invalid-response' | 'configuration';

export class ApiError extends Error {
  readonly status: number | null;
  readonly errors: JsonApiError[];
  readonly kind: ApiErrorKind;

  constructor(
    message: string,
    options: { status?: number; errors?: JsonApiError[]; kind?: ApiErrorKind } = {},
  ) {
    super(message);
    this.name = 'ApiError';
    this.status = options.status ?? null;
    this.errors = options.errors ?? [];
    this.kind = options.kind ?? 'http';
  }

  getFieldErrors(): Record<string, string[]> {
    const fields: Record<string, string[]> = Object.create(null);
    for (const error of this.errors) {
      const field = error.meta?.field;
      const message = error.detail ?? error.title;
      if (field && message) (fields[field] ??= []).push(message);
    }
    return fields;
  }
}

export function readJsonApiErrors(value: unknown): JsonApiError[] {
  if (!value || typeof value !== 'object' || !('errors' in value)) return [];
  if (!Array.isArray(value.errors)) return [];

  return value.errors.flatMap((entry: unknown) => {
    if (!entry || typeof entry !== 'object') return [];
    const record = entry as Record<string, unknown>;
    const error: JsonApiError = {};
    for (const key of ['id', 'status', 'code', 'title', 'detail'] as const) {
      if (typeof record[key] === 'string') error[key] = record[key];
    }
    if ('meta' in entry && entry.meta && typeof entry.meta === 'object') {
      if ('field' in entry.meta && typeof entry.meta.field === 'string') {
        error.meta = { field: entry.meta.field };
      }
    }
    return [error];
  });
}
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="api-error.ts",
            content=content
        )
        
        
        
    def create_api_ts(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "api")
    
        content = r'''// src/api/api.ts
import { ApiError, readJsonApiErrors } from "./api-error";
import { authTokenStorage } from "@/modules/auth/services/authTokenStorage";

export interface ApiOptions {
  method?: "GET" | "POST" | "PUT" | "PATCH" | "DELETE";
  body?: unknown;
  token?: string | null;
  signal?: AbortSignal;
  contentType?: "json" | "jsonapi";
  skipAuth?: boolean;
}

const REQUEST_TIMEOUT_MS = 15_000;

function getUrl(endpoint: string): string {
  const baseUrl = import.meta.env.VITE_API_URL?.trim();

  if (!baseUrl) {
    throw new ApiError("Falta configurar VITE_API_URL.", {
      kind: "configuration",
    });
  }

  try {
    const base = new URL(`${baseUrl.replace(/\/+$/, "")}/`);
    const url = new URL(endpoint.replace(/^\/+/, ""), base);

    if (
      !["http:", "https:"].includes(base.protocol) ||
      url.origin !== base.origin ||
      !url.pathname.startsWith(base.pathname)
    ) {
      throw new Error("Invalid API URL");
    }

    return url.toString();
  } catch {
    throw new ApiError(
      "La URL de la API o el endpoint no es válido.",
      { kind: "configuration" }
    );
  }
}

async function request(
  endpoint: string,
  options: ApiOptions,
  responseType: "json" | "blob"
): Promise<unknown> {
  const url = getUrl(endpoint);

  const headers = new Headers({
    Accept:
      responseType === "json"
        ? "application/vnd.api+json"
        : "*/*",
  });

  // Content-Type configurable para endpoints no JSON:API.
  if (options.body !== undefined) {
    headers.set(
      "Content-Type",
      options.contentType === "json"
        ? "application/json"
        : "application/vnd.api+json"
    );
  }

  // Obtener automáticamente el token de la sesión.
  const token = options.skipAuth
    ? null
    : options.token !== undefined
      ? options.token
      : authTokenStorage.get();

  if (token) {
    const scheme = import.meta.env.VITE_AUTH_SCHEME || "Bearer";
    headers.set("Authorization", `${scheme} ${token}`);
  }

  const timeout = AbortSignal.timeout(REQUEST_TIMEOUT_MS);

  const signal = options.signal
    ? AbortSignal.any([options.signal, timeout])
    : timeout;

  try {
    const response = await fetch(url, {
      method: options.method ?? "GET",
      headers,
      body:
        options.body === undefined
          ? undefined
          : JSON.stringify(options.body),
      signal,
    });

    if (response.ok && responseType === "blob") {
      return await response.blob();
    }

    const text = await response.text();

    let payload: unknown;

    try {
      payload = text ? JSON.parse(text) : undefined;
    } catch {
      throw new ApiError(
        response.ok
          ? "La API no devolvió un JSON válido."
          : `Error HTTP ${response.status}.`,
        {
          status: response.status,
          kind: response.ok ? "invalid-response" : "http",
        }
      );
    }

    const errors = readJsonApiErrors(payload);

    if (!response.ok || errors.length > 0) {
      throw new ApiError(
        errors[0]?.detail ??
          errors[0]?.title ??
          `Error HTTP ${response.status}.`,
        {
          status: response.status,
          errors,
        }
      );
    }

    return payload;
  } catch (error) {
    if (error instanceof ApiError) throw error;

    if (options.signal?.aborted) throw error;

    if (timeout.aborted) {
      throw new ApiError(
        "La API ha tardado demasiado en responder.",
        { kind: "timeout" }
      );
    }

    throw new ApiError(
      "No se pudo conectar con la API.",
      { kind: "network" }
    );
  }
}

export async function api<T = unknown>(
  endpoint: string,
  options: ApiOptions = {}
): Promise<T | undefined> {
  return (await request(endpoint, options, "json")) as
    | T
    | undefined;
}

export async function apiBlob(
  endpoint: string,
  options: ApiOptions = {}
): Promise<Blob> {
  return (await request(endpoint, options, "blob")) as Blob;
}
'''
        
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="api.ts",
            content=content
        )
            
    
    def create_json_api_types_ts(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "api")
    
        content = r'''// src/api/json-api.types.ts
export interface JsonApiResource<TAttributes, TType extends string = string> {
  type: TType;
  id: string;
  attributes: TAttributes;
}

export interface JsonApiDocument<TData> {
  data: TData;
  meta?: Record<string, unknown>;
  links?: Record<string, unknown>;
  included?: JsonApiResource<Record<string, unknown>>[];
}

export interface JsonApiError {
  id?: string;
  status?: string;
  code?: string;
  title?: string;
  detail?: string;
  source?: { pointer?: string; parameter?: string; header?: string };
  meta?: { field?: string; [key: string]: unknown };
}

export interface JsonApiErrorDocument {
  errors: JsonApiError[];
}
'''
        
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="json-api.types.ts",
            content=content
        )
            
    
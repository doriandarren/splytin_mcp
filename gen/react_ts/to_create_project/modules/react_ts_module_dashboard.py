import os
from helpers.helper_columns import HelperColumns
from helpers.helper_file import HelperFile
from gen.react_ts.to_create_module_crud.standard_module_crud_react_ts import StandardModuleCrudReactTs
from helpers.helper_print import dd, print_green, print_red


class ReactTsModuleDashboard:
    
    def invoke(self, full_path):
        self.create_module(full_path)
        self.replace_dashboard_page_tsx(full_path)
        self.create_dashboard_page_css(full_path)
        self.create_dashboard_stats_tsx(full_path)
        self.create_dashboard_stat_card_tsx(full_path)
        self.create_dashboard_activity_chart_tsx(full_path)
        self.update_app_router_tsx(full_path)
        self.replace_dashboards_routes_tsx(full_path)
        self.delete_files(full_path)
    
    
    
    def create_module(self, full_path):
        columns = HelperColumns.parse_columns_input("total_customers:int total_invoices:int total_income:decimal total_expenses:decimal")

        obj = StandardModuleCrudReactTs()
        obj.invoke(
            full_path=full_path,
            namespace="private",
            singular_name="Dashboard",
            plural_name="Dashboards",
            columns=columns,
            input_menu_checkbox=None,
            version_api="V1",
            folder_group="api"
        )

    
    
    def replace_dashboard_page_tsx(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "private", "dashboards", "pages")

        content = r'''// src/modules/private/dashboards/pages/DashboardPage.tsx
import { useTranslation } from "react-i18next";

import { DashboardActivityChart } from "../components/DashboardActivityChart";
import { DashboardStats } from "../components/DashboardStats";
import { useDashboards } from "../hooks/useDashboards";

import type { DashboardAttributes } from "../types/dashboard.types";

import "./DashboardPage.css";

// Valores por defecto
const defaultStats: DashboardAttributes = {
    total_customers: 0,
    total_invoices: 0,
    total_income: 0,
    total_expenses: 0,
    created_at: "",
    updated_at: "",
};

export const DashboardPage = () => {
    // Traducciones
    const { t } = useTranslation();

    // Obtener información de la API
    const query = useDashboards();

    // Primer registro del listado
    const dashboard = query.data?.data?.[0];

    // Estadísticas
    const stats = dashboard?.attributes ?? defaultStats;

    return (
        <div className="dashboard-page">

            {/* Encabezado del dashboard */}
            <div className="dashboard-header">
                <div>
                    <h1 className="dashboard-title">
                        {t("dashboard_module.title")}
                    </h1>

                    <p className="dashboard-subtitle">
                        {t("dashboard_module.subtitle")}
                    </p>
                </div>
            </div>


            {/* Tarjetas de estadísticas */}
            {!query.isPending && !query.isError && (
                <>
                    <DashboardStats data={stats} />
                </>
            )}

            {/* Gráfico financiero */}
            <DashboardActivityChart />

        </div>
    );
};
'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="DashboardPage.tsx",
            content=content
        )


    
    def create_dashboard_page_css(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "private", "dashboards", "pages")

        content = r'''@reference "../../../../index.css";


@layer components {


    /* ============================================
        DASHBOARD - PAGE
    ============================================ */


    .dashboard-page {
        @apply flex flex-col gap-6;
    }


    .dashboard-header {
        @apply flex items-center justify-between;
    }


    .dashboard-title {
        @apply text-2xl font-semibold tracking-tight text-foreground;
    }


    .dashboard-subtitle {
        @apply mt-1 text-sm text-muted-foreground;
    }


    /* ============================================
        DASHBOARD - STATS
    ============================================ */


    .dashboard-stats-grid {
        @apply grid grid-cols-1 gap-4;
        @apply sm:grid-cols-2 xl:grid-cols-4;
    }


    .dashboard-stat-card {
        @apply rounded-xl border border-border bg-card p-5;
        @apply text-foreground shadow-sm;
        @apply transition-all duration-300 ease-out;
    }


    .dashboard-stat-card:hover {
        @apply -translate-y-1 shadow-md;
    }


    .dashboard-stat-header {
        @apply flex items-center justify-between;
        @apply text-sm font-medium text-muted-foreground;
    }


    .dashboard-stat-icon {
        @apply text-primary;
        @apply transition-transform duration-300;
    }


    .dashboard-stat-card:hover .dashboard-stat-icon {
        @apply scale-110;
    }


    .dashboard-stat-value {
        @apply mt-3 text-3xl font-semibold tracking-tight;
        @apply text-primary;
    }


    .dashboard-stat-description {
        @apply mt-1 text-xs text-muted-foreground;
    }


    /* ============================================
        DASHBOARD - STAT COLORS
    ============================================ */


    /* Clientes - Verde */


    .dashboard-stat-customers {
        border-top: 3px solid #10b981;
    }


    .dashboard-stat-customers .dashboard-stat-icon {
        color: #10b981;
    }


    /* Facturas - Azul corporativo */


    .dashboard-stat-invoices {
        border-top: 3px solid var(--primary);
    }


    .dashboard-stat-invoices .dashboard-stat-icon {
        color: var(--primary);
    }


    /* Ingresos - Azul petróleo */


    .dashboard-stat-income {
        border-top: 3px solid #17618a;
    }


    .dashboard-stat-income .dashboard-stat-icon {
        color: #17618a;
    }


    /* Gastos - Coral */


    .dashboard-stat-expenses {
        border-top: 3px solid #f97360;
    }


    .dashboard-stat-expenses .dashboard-stat-icon {
        color: #f97360;
    }


    /* ============================================
        DASHBOARD - CHART
    ============================================ */


    .dashboard-chart {
        @apply rounded-xl border border-border bg-card p-5 md:p-6;
        @apply text-foreground shadow-sm;
    }


    .dashboard-chart-header {
        @apply mb-6 flex flex-wrap items-center justify-between gap-3;
    }


    .dashboard-chart-title {
        @apply text-base font-semibold text-foreground;
    }


    .dashboard-chart-description {
        @apply mt-1 text-sm text-muted-foreground;
    }


    .dashboard-chart-period {
        @apply rounded-md bg-secondary px-3 py-1.5;
        @apply text-xs font-medium text-secondary-foreground;
    }


    .dashboard-chart-container {
        @apply h-[280px] w-full md:h-[340px];
    }


    /* ============================================
        DASHBOARD - ACCESSIBILITY
    ============================================ */


    @media (prefers-reduced-motion: reduce) {


        .dashboard-stat-card,
        .dashboard-stat-icon {
            transition: none;
        }


        .dashboard-stat-card:hover,
        .dashboard-stat-card:hover .dashboard-stat-icon {
            transform: none;
        }
    }


}'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="DashboardPage.css",
            content=content
        )
    
    
    
    def create_dashboard_stats_tsx(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "modules", "private", "dashboards", "components")
    
        content = r'''// src/modules/private/dashboards/components/DashboardStats.tsx
import { useTranslation } from "react-i18next";

import {
    Users,
    ReceiptText,
    TrendingUp,
    Wallet,
} from "lucide-react";

import { DashboardStatCard } from "./DashboardStatCard";
import type { DashboardAttributes } from "../types/dashboard.types";

// Formato numérico español
const numberFormatter = new Intl.NumberFormat("es-ES");

// Formato de moneda
const currencyFormatter = new Intl.NumberFormat("es-ES", {
    style: "currency",
    currency: "EUR",
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
    useGrouping: true,
});

interface Props {
    data: DashboardAttributes;
}

export const DashboardStats = ({ data }: Props) => {
    const { t } = useTranslation();

    return (
        <div className="dashboard-stats-grid">

            <DashboardStatCard
                title={t("dashboard_module.stats.total_customers")}
                value={numberFormatter.format(data.total_customers)}
                description={t("dashboard_module.stats.customers_description")}
                icon={<Users size={21} />}
                variant="customers"
            />

            <DashboardStatCard
                title={t("dashboard_module.stats.total_invoices")}
                value={numberFormatter.format(data.total_invoices)}
                description={t("dashboard_module.stats.invoices_description")}
                icon={<ReceiptText size={21} />}
                variant="invoices"
            />

            <DashboardStatCard
                title={t("dashboard_module.stats.total_income")}
                value={currencyFormatter.format(Number(data.total_income))}
                description={t("dashboard_module.stats.income_description")}
                icon={<TrendingUp size={21} />}
                variant="income"
            />

            <DashboardStatCard
                title={t("dashboard_module.stats.total_expenses")}
                value={currencyFormatter.format(Number(data.total_expenses))}
                description={t("dashboard_module.stats.expenses_description")}
                icon={<Wallet size={21} />}
                variant="expenses"
            />

        </div>
    );
};
'''

    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="DashboardStats.tsx",
            content=content
        )
    
    
    
    
    def create_dashboard_stat_card_tsx(self, full_path):
        """
        Genera el archivo.
        """

        folder_path = os.path.join(full_path, "src", "modules", "private", "dashboards", "components")

        content = r'''// src/modules/private/dashboards/components/DashboardStatCard.tsx

import type { ReactNode } from "react";

type StatVariant =
    | "customers"
    | "invoices"
    | "income"
    | "expenses";

interface DashboardStatCardProps {
    title: string;
    value: string | number;
    description?: string;
    icon?: ReactNode;
    variant?: StatVariant;
}

export const DashboardStatCard = ({
    title,
    value,
    description,
    icon,
    variant = "invoices",
}: DashboardStatCardProps) => {
    return (
        <div className={`dashboard-stat-card dashboard-stat-${variant}`}>
            <div className="dashboard-stat-header">
                <span>{title}</span>

                {icon && (
                    <span className="dashboard-stat-icon">
                        {icon}
                    </span>
                )}
            </div>

            <div className="dashboard-stat-value">
                {value}
            </div>

            {description && (
                <p className="dashboard-stat-description">
                    {description}
                </p>
            )}
        </div>
    );
};'''

        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="DashboardStatCard.tsx",
            content=content
        )
    
    
    
    
    def create_dashboard_activity_chart_tsx(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "modules", "private", "dashboards", "components")
    
        content = r'''// src/modules/private/dashboards/components/DashboardActivityChart.tsx
import { useTranslation } from "react-i18next";
import {
    Area,
    AreaChart,
    CartesianGrid,
    XAxis,
    YAxis,
} from "recharts";

import {
    ChartContainer,
    ChartLegend,
    ChartLegendContent,
    ChartTooltip,
    ChartTooltipContent,
    type ChartConfig,
} from "@/components/ui/chart";

// Datos de ejemplo
const chartData = [
    { month: "Jun", total_customers: 125, total_invoices: 85, total_income: 12000, total_expenses: 6500 },
    { month: "Jul", total_customers: 155, total_invoices: 110, total_income: 17500, total_expenses: 8200 },
    { month: "Ago", total_customers: 138, total_invoices: 95, total_income: 14800, total_expenses: 7000 },
    { month: "Sep", total_customers: 220, total_invoices: 160, total_income: 21500, total_expenses: 9300 },
    { month: "Oct", total_customers: 192, total_invoices: 145, total_income: 19200, total_expenses: 7800 },
    { month: "Nov", total_customers: 265, total_invoices: 210, total_income: 26500, total_expenses: 8450 },
];

// Colores del gráfico
const chartConfig = {
    total_customers: {
        label: "Clientes",
        color: "#10b981", // Verde esmeralda
    },
    total_invoices: {
        label: "Facturas",
        color: "var(--chart-1)", // Azul corporativo
    },
    total_income: {
        label: "Ingresos",
        color: "#8b5cf6", // Violeta
    },
    total_expenses: {
        label: "Gastos",
        color: "#f97360", // Coral
    },
} satisfies ChartConfig;

// Formato numérico
const numberFormatter = new Intl.NumberFormat("es-ES");

// Formato de moneda
const currencyFormatter = new Intl.NumberFormat("es-ES", {
    style: "currency",
    currency: "EUR",
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
    useGrouping: true,
});

export const DashboardActivityChart = () => {
    const { t } = useTranslation();

    // Traducciones de las series
    const translatedChartConfig = {
        total_customers: {
            ...chartConfig.total_customers,
            label: t("dashboard_module.stats.total_customers"),
        },
        total_invoices: {
            ...chartConfig.total_invoices,
            label: t("dashboard_module.stats.total_invoices"),
        },
        total_income: {
            ...chartConfig.total_income,
            label: t("dashboard_module.stats.total_income"),
        },
        total_expenses: {
            ...chartConfig.total_expenses,
            label: t("dashboard_module.stats.total_expenses"),
        },
    } satisfies ChartConfig;

    return (
        <section className="dashboard-chart">

            {/* Encabezado */}
            <div className="dashboard-chart-header">
                <div>
                    <h2 className="dashboard-chart-title">
                        {t("dashboard_module.chart.title")}
                    </h2>

                    <p className="dashboard-chart-description">
                        {t("dashboard_module.chart.description")}
                    </p>
                </div>

                <span className="dashboard-chart-period">
                    {t("dashboard_module.chart.period")}
                </span>
            </div>

            {/* Gráfico */}
            <ChartContainer
                config={translatedChartConfig}
                className="dashboard-chart-container"
            >
                <AreaChart
                    accessibilityLayer
                    data={chartData}
                    margin={{
                        top: 12,
                        right: 12,
                        left: 0,
                        bottom: 0,
                    }}
                >

                    {/* Degradados */}
                    <defs>
                        <linearGradient id="dashboardCustomersGradient" x1="0" y1="0" x2="0" y2="1">
                            <stop offset="5%" stopColor="var(--color-total_customers)" stopOpacity={0.18} />
                            <stop offset="95%" stopColor="var(--color-total_customers)" stopOpacity={0} />
                        </linearGradient>

                        <linearGradient id="dashboardInvoicesGradient" x1="0" y1="0" x2="0" y2="1">
                            <stop offset="5%" stopColor="var(--color-total_invoices)" stopOpacity={0.18} />
                            <stop offset="95%" stopColor="var(--color-total_invoices)" stopOpacity={0} />
                        </linearGradient>

                        <linearGradient id="dashboardIncomeGradient" x1="0" y1="0" x2="0" y2="1">
                            <stop offset="5%" stopColor="var(--color-total_income)" stopOpacity={0.28} />
                            <stop offset="95%" stopColor="var(--color-total_income)" stopOpacity={0} />
                        </linearGradient>

                        <linearGradient id="dashboardExpensesGradient" x1="0" y1="0" x2="0" y2="1">
                            <stop offset="5%" stopColor="var(--color-total_expenses)" stopOpacity={0.22} />
                            <stop offset="95%" stopColor="var(--color-total_expenses)" stopOpacity={0} />
                        </linearGradient>
                    </defs>

                    {/* Cuadrícula */}
                    <CartesianGrid
                        vertical={false}
                        stroke="var(--border)"
                        strokeDasharray="3 3"
                    />

                    {/* Eje horizontal */}
                    <XAxis
                        dataKey="month"
                        tickLine={false}
                        axisLine={false}
                        tickMargin={12}
                    />

                    {/* Eje izquierdo: cantidades */}
                    <YAxis
                        yAxisId="quantity"
                        orientation="left"
                        tickLine={false}
                        axisLine={false}
                        tickMargin={8}
                        width={42}
                        tickFormatter={(value: number) =>
                            numberFormatter.format(value)
                        }
                    />

                    {/* Eje derecho: euros */}
                    <YAxis
                        yAxisId="currency"
                        orientation="right"
                        tickLine={false}
                        axisLine={false}
                        tickMargin={8}
                        width={55}
                        tickFormatter={(value: number) =>
                            `${numberFormatter.format(value / 1000)}k €`
                        }
                    />

                    {/* Tooltip */}
                    <ChartTooltip
                        cursor={false}
                        content={
                            <ChartTooltipContent
                                indicator="dot"
                                formatter={(value, name) => {
                                    const key = String(name);
                                    const isCurrency =
                                        key === "total_income" ||
                                        key === "total_expenses";

                                    const label =
                                        translatedChartConfig[
                                            key as keyof typeof translatedChartConfig
                                        ]?.label ?? key;

                                    return (
                                        <span className="text-foreground">
                                            {label}:{" "}
                                            {isCurrency
                                                ? currencyFormatter.format(Number(value))
                                                : numberFormatter.format(Number(value))}
                                        </span>
                                    );
                                }}
                            />
                        }
                    />

                    {/* Clientes */}
                    <Area
                        yAxisId="quantity"
                        type="monotone"
                        dataKey="total_customers"
                        stroke="var(--color-total_customers)"
                        strokeWidth={2.5}
                        fill="url(#dashboardCustomersGradient)"
                        fillOpacity={1}
                        dot={false}
                        activeDot={{ r: 5 }}
                        isAnimationActive
                        animationBegin={100}
                        animationDuration={1300}
                    />

                    {/* Facturas */}
                    <Area
                        yAxisId="quantity"
                        type="monotone"
                        dataKey="total_invoices"
                        stroke="var(--color-total_invoices)"
                        strokeWidth={2.5}
                        fill="url(#dashboardInvoicesGradient)"
                        fillOpacity={1}
                        dot={false}
                        activeDot={{ r: 5 }}
                        isAnimationActive
                        animationBegin={200}
                        animationDuration={1300}
                    />

                    {/* Ingresos */}
                    <Area
                        yAxisId="currency"
                        type="monotone"
                        dataKey="total_income"
                        stroke="var(--color-total_income)"
                        strokeWidth={2.5}
                        fill="url(#dashboardIncomeGradient)"
                        fillOpacity={1}
                        dot={false}
                        activeDot={{ r: 5 }}
                        isAnimationActive
                        animationBegin={300}
                        animationDuration={1400}
                    />

                    {/* Gastos */}
                    <Area
                        yAxisId="currency"
                        type="monotone"
                        dataKey="total_expenses"
                        stroke="var(--color-total_expenses)"
                        strokeWidth={2.5}
                        fill="url(#dashboardExpensesGradient)"
                        fillOpacity={1}
                        dot={false}
                        activeDot={{ r: 5 }}
                        isAnimationActive
                        animationBegin={400}
                        animationDuration={1500}
                    />

                    {/* Leyenda */}
                    <ChartLegend content={<ChartLegendContent />} />

                </AreaChart>
            </ChartContainer>
        </section>
    );
};
'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="DashboardActivityChart.tsx",
            content=content
        )
    
    
    
    
    def update_app_router_tsx(self, full_path):
        """
        Actualiza el archivo
        """
        main_path = os.path.join(full_path, "src", "app.router.tsx")
    
        # Verificar si el archivo existe
        if not os.path.exists(main_path):
            print_red(f"Error: {main_path} no existe.")
            dd(f"Error: {main_path} no existe.")
            return False
    
        try:
            # Leer el contenido del archivo
            with open(main_path, "r", encoding="utf-8") as f:
                content = f.read()
    
    

            # Reemplazos
            replacements = {
                ## New Item -> KEY : VALUE
                """            ...dashboardRoutes,""":
                """     {
            index: true,
            element: <DashboardPage />,
          },""",
                """// CRUD IMPORTS""":
                """import { DashboardPage } from "./modules/private/dashboards/pages/DashboardPage";
// CRUD IMPORTS""",
                """import { ProtectedRoute } from "./modules/auth/components/ProtectedRoute";
import { dashboardRoutes } from "./modules/private/dashboards/routes/dashboards.routes";""":
                """import { ProtectedRoute } from "./modules/auth/components/ProtectedRoute";"""
            }
    
            # Validar y aplicar los reemplazos
            new_content = content
    
            for old_text, new_text in replacements.items():
                if old_text not in new_content:
                    raise ValueError(f"No se encontró el texto esperado: {old_text}")
    
                new_content = new_content.replace(old_text, new_text, 1)
    
            if new_content == content:
                raise ValueError("No se realizó ningún reemplazo.")
    
            # Escribir el contenido actualizado
            with open(main_path, "w", encoding="utf-8") as f:
                f.write(new_content)
    
            print_green(f"{main_path} actualizado correctamente.")
    
            return True
    
        except Exception as e:
            print_red(f"Error al actualizar {main_path}: {e}")
            return False




    def replace_dashboards_routes_tsx(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "modules", "private", "dashboards", "routes")
    
        content = r'''// src/modules/private/dashboards/routes/dashboards.routes.tsx
import type { RouteObject } from "react-router";

// import { DashboardPage } from "../pages/DashboardPage";
// import { DashboardCreatePage } from "../pages/DashboardCreatePage";
// import { DashboardUpdatePage } from "../pages/DashboardUpdatePage";

export const dashboardRoutes: RouteObject[] = [
    // {
    //     path: "dashboards",
    //     element: <DashboardPage />,
    // },
    // {
    //     path: "dashboards/create",
    //     element: <DashboardCreatePage />,
    // },
    // {
    //     path: "dashboards/:id/edit",
    //     element: <DashboardUpdatePage />,
    // },
];'''
    
        # Crear el archivo
        HelperFile.write(
            folder_path=folder_path,
            file_name="dashboards.routes.tsx",
            content=content
        )
    



    def delete_files(self, full_path):
        """
        Elimina un archivo del proyecto.
        """
        # Delete file
        folder_path = os.path.join(full_path, "src", "modules", "private", "dashboards", "pages")
        file_path = os.path.join(folder_path, "DashboardCreatePage.tsx")
    
        if os.path.isfile(file_path):
            os.remove(file_path)
            print_green(f"Archivo Eliminado: {file_path}")
            
            
            
        # Delete file
        folder_path = os.path.join(full_path, "src", "modules", "private", "dashboards", "pages")
        file_path = os.path.join(folder_path, "DashboardUpdatePage.tsx")

        if os.path.isfile(file_path):
            os.remove(file_path)
            print_green(f"Archivo Eliminado: {file_path}")



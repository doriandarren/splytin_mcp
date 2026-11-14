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
import { DashboardActivityChart } from "../components/DashboardActivityChart";
import { DashboardStats } from "../components/DashboardStats";
import "./DashboardPage.css";

export const DashboardPage = () => {
    return (
        <div className="dashboard-page">

            {/* Encabezado del dashboard */}
            <div className="dashboard-header">
                <div>
                    <h1 className="dashboard-title">
                        Dashboard
                    </h1>

                    <p className="dashboard-subtitle">
                        Bienvenido a tu panel de administración
                    </p>
                </div>
            </div>

            {/* Tarjetas de estadísticas */}
            <DashboardStats />

            {/* Gráfico de barras */}
            <DashboardActivityChart />

        </div>
    );
};'''

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

import {
    Users,
    ReceiptText,
    TrendingUp,
    Wallet,
} from "lucide-react";

import { DashboardStatCard } from "./DashboardStatCard";

// Datos ficticios con la estructura de la API
const dashboardData = {
    total_customers: 248,
    total_invoices: 1284,
    total_income: "26500.00",
    total_expenses: "8450.00",
};

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

export const DashboardStats = () => {
    return (
        <div className="dashboard-stats-grid">

            <DashboardStatCard
                title="Total clientes"
                value={numberFormatter.format(
                    dashboardData.total_customers
                )}
                description="Clientes registrados"
                icon={<Users size={21} />}
                variant="customers"
            />

            <DashboardStatCard
                title="Total facturas"
                value={numberFormatter.format(
                    dashboardData.total_invoices
                )}
                description="Facturas registradas"
                icon={<ReceiptText size={21} />}
                variant="invoices"
            />

            <DashboardStatCard
                title="Total ingresos"
                value={currencyFormatter.format(
                    Number(dashboardData.total_income)
                )}
                description="Ingresos acumulados"
                icon={<TrendingUp size={21} />}
                variant="income"
            />

            <DashboardStatCard
                title="Total gastos"
                value={currencyFormatter.format(
                    Number(dashboardData.total_expenses)
                )}
                description="Gastos acumulados"
                icon={<Wallet size={21} />}
                variant="expenses"
            />

        </div>
    );
};'''
    
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
import { Area, AreaChart, CartesianGrid, XAxis, YAxis } from "recharts";

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
    { month: "Jun", lavados: 125, clientes: 32 },
    { month: "Jul", lavados: 155, clientes: 45 },
    { month: "Ago", lavados: 138, clientes: 41 },
    { month: "Sep", lavados: 220, clientes: 62 },
    { month: "Oct", lavados: 192, clientes: 75 },
    { month: "Nov", lavados: 265, clientes: 89 },
];

// Colores definidos en index.css

const chartConfig = {
    lavados: {
        label: "Lavados",
        color: "var(--chart-1)", // Azul del tema actual
    },
    clientes: {
        label: "Clientes",
        color: "#10b981", // Verde esmeralda
    },
} satisfies ChartConfig;

export const DashboardActivityChart = () => {
    return (
        <section className="dashboard-chart">
            {/* Encabezado */}
            <div className="dashboard-chart-header">
                <div>
                    <h2 className="dashboard-chart-title">Actividad general</h2>

                    <p className="dashboard-chart-description">
                        Evolución de clientes y lavados
                    </p>
                </div>

                <span className="dashboard-chart-period">Últimos 6 meses</span>
            </div>

            {/* Gráfico */}
            <ChartContainer
                config={chartConfig}
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
                        <linearGradient
                            id="dashboardLavadosGradient"
                            x1="0"
                            y1="0"
                            x2="0"
                            y2="1"
                        >
                            <stop
                                offset="5%"
                                stopColor="var(--color-lavados)"
                                stopOpacity={0.55}
                            />
                            <stop
                                offset="95%"
                                stopColor="var(--color-lavados)"
                                stopOpacity={0}
                            />
                        </linearGradient>

                        <linearGradient
                            id="dashboardClientesGradient"
                            x1="0"
                            y1="0"
                            x2="0"
                            y2="1"
                        >
                            <stop
                                offset="5%"
                                stopColor="var(--color-clientes)"
                                stopOpacity={0.35}
                            />
                            <stop
                                offset="95%"
                                stopColor="var(--color-clientes)"
                                stopOpacity={0}
                            />
                        </linearGradient>
                    </defs>

                    {/* Cuadrícula */}
                    <CartesianGrid
                        vertical={false}
                        stroke="var(--border)"
                        strokeDasharray="3 3"
                    />

                    {/* Ejes */}
                    <XAxis
                        dataKey="month"
                        tickLine={false}
                        axisLine={false}
                        tickMargin={12}
                    />

                    <YAxis tickLine={false} axisLine={false} tickMargin={8} width={35} />

                    {/* Tooltip */}
                    <ChartTooltip
                        cursor={false}
                        content={<ChartTooltipContent indicator="dot" />}
                    />

                    {/* Lavados */}
                    <Area
                        type="monotone"
                        dataKey="lavados"
                        stroke="var(--color-lavados)"
                        strokeWidth={2.5}
                        fill="url(#dashboardLavadosGradient)"
                        fillOpacity={1}
                        dot={false}
                        activeDot={{ r: 5 }}
                        isAnimationActive
                        animationBegin={200}
                        animationDuration={1300}
                    />

                    {/* Clientes */}
                    <Area
                        type="monotone"
                        dataKey="clientes"
                        stroke="var(--color-clientes)"
                        strokeWidth={2.5}
                        fill="url(#dashboardClientesGradient)"
                        fillOpacity={1}
                        dot={false}
                        activeDot={{ r: 5 }}
                        isAnimationActive
                        animationBegin={300}
                        animationDuration={1500}
                    />

                    {/* Leyenda */}
                    <ChartLegend content={<ChartLegendContent />} />
                </AreaChart>
            </ChartContainer>
        </section>
    );
};'''
    
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



import os
from helpers.helper_columns import HelperColumns
from helpers.helper_file import HelperFile
from gen.react_ts.to_create_module_crud.standard_module_crud_react_ts import StandardModuleCrudReactTs


class ReactTsModuleDashboard:
    
    def invoke(self, full_path):
        self.create_module(full_path)
        self.replace_dashboard_page_tsx(full_path)
        self.create_dashboard_stats_tsx(full_path)
        self.create_dashboard_stat_card_tsx(full_path)
        self.create_dashboard_activity_chart_tsx(full_path)
    
    
    
    def create_module(self, full_path):
        columns = HelperColumns.parse_columns_input("name")

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

    
    
    def create_dashboard_stats_tsx(self, full_path):
        """
        Genera el archivo.
        """
    
        folder_path = os.path.join(full_path, "src", "modules", "private", "dashboards", "components")
    
        content = r'''// src/modules/private/dashboards/components/DashboardStats.tsx
import { Users, Server, Droplets } from "lucide-react";

import { DashboardStatCard } from "./DashboardStatCard";

export const DashboardStats = () => {
    return (
        <div className="dashboard-stats-grid">
            <DashboardStatCard
                title="Clientes"
                value={248}
                description="Total registrados"
                icon={<Users size={20} />}
            />

            <DashboardStatCard
                title="Sistemas"
                value={36}
                description="Total registrados"
                icon={<Server size={20} />}
            />

            <DashboardStatCard
                title="Lavados"
                value={1284}
                description="Total realizados"
                icon={<Droplets size={20} />}
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

interface DashboardStatCardProps {
    title: string;
    value: string | number;
    description?: string;
    icon?: ReactNode;
}

export const DashboardStatCard = ({
    title,
    value,
    description,
    icon,
}: DashboardStatCardProps) => {
    return (
        <div className="dashboard-stat-card">
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
    
    
    
    
    

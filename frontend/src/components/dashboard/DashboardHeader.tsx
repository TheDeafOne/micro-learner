import { Badge } from "@/components/ui/badge";

import type { ActionMessage } from "@/hooks/useDashboardData";

interface DashboardHeaderProps {
  apiBaseUrl: string;
  healthStatus: string | null;
  healthError: string | null;
  actionMessage: ActionMessage | null;
}

export function DashboardHeader({
  apiBaseUrl,
  healthStatus,
  healthError,
  actionMessage,
}: DashboardHeaderProps) {
  return (
    <header className="border-b bg-card">
      <div className="container flex flex-col gap-2 py-6 md:flex-row md:items-center md:justify-between">
        <div>
          <h1 className="text-2xl font-semibold tracking-tight">
            Canvas Summarization Dashboard
          </h1>
          <p className="text-sm text-muted-foreground">
            Connected to <span className="font-mono">{apiBaseUrl}</span>
          </p>
        </div>
        <div className="flex flex-wrap items-center gap-2 text-sm text-muted-foreground">
          <span>
            Health:{" "}
            {healthError ? (
              <span className="text-destructive">{healthError}</span>
            ) : healthStatus ? (
              <span className="text-emerald-600 dark:text-emerald-400">
                {healthStatus}
              </span>
            ) : (
              "Checking…"
            )}
          </span>
          {actionMessage && (
            <Badge
              variant={actionMessage.type === "success" ? "secondary" : "destructive"}
              className="font-normal"
            >
              {actionMessage.text}
            </Badge>
          )}
        </div>
      </div>
    </header>
  );
}

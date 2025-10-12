import type { Module } from "@/types";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { ScrollArea } from "@/components/ui/scroll-area";
import { cn } from "@/lib/utils";
import { formatDateTime } from "@/lib/format";

interface ModuleListPanelProps {
  modules: Module[];
  selectedModuleId: number | null;
  onSelectModule: (moduleId: number) => void;
  loading: boolean;
  error: string | null;
  onRefresh: () => Promise<void>;
  refreshing: boolean;
  courseName: string | null;
}

export function ModuleListPanel({
  modules,
  selectedModuleId,
  onSelectModule,
  loading,
  error,
  onRefresh,
  refreshing,
  courseName,
}: ModuleListPanelProps) {
  return (
    <Card>
      <CardHeader className="flex flex-row items-center justify-between space-y-0">
        <div>
          <CardTitle className="text-lg">Modules</CardTitle>
          <CardDescription>
            Modules for {courseName ? courseName : "…"}
          </CardDescription>
        </div>
        <Button
          size="sm"
          variant="outline"
          onClick={onRefresh}
          disabled={refreshing || !courseName}
        >
          {refreshing ? "Refreshing…" : "Refresh"}
        </Button>
      </CardHeader>
      <CardContent>
        {error ? (
          <p className="text-sm text-destructive">{error}</p>
        ) : loading ? (
          <p className="text-sm text-muted-foreground">Loading modules…</p>
        ) : modules.length === 0 ? (
          <p className="text-sm text-muted-foreground">
            {courseName
              ? "No modules found. Refresh to sync from Canvas."
              : "Select a course to view its modules."}
          </p>
        ) : (
          <ScrollArea className="h-[420px]">
            <div className="space-y-2">
              {modules.map((module) => (
                <button
                  key={module.id}
                  type="button"
                  onClick={() => onSelectModule(module.id)}
                  className={cn(
                    "w-full rounded-md border px-3 py-2 text-left transition-colors hover:bg-accent",
                    selectedModuleId === module.id
                      ? "border-primary bg-accent"
                      : "border-transparent",
                  )}
                >
                  <div className="font-medium">{module.title}</div>
                  <div className="text-xs text-muted-foreground">
                    Position {module.position ?? "—"} · Last synced{" "}
                    {formatDateTime(module.last_synced_at)}
                  </div>
                </button>
              ))}
            </div>
          </ScrollArea>
        )}
      </CardContent>
    </Card>
  );
}

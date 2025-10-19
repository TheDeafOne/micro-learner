import type { Course } from "@/types";
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

interface CourseListPanelProps {
  courses: Course[];
  selectedCourseId: number | null;
  onSelectCourse: (courseId: number) => void;
  loading: boolean;
  error: string | null;
  onRefresh: () => Promise<void>;
  refreshing: boolean;
}

export function CourseListPanel({
  courses,
  selectedCourseId,
  onSelectCourse,
  loading,
  error,
  onRefresh,
  refreshing,
}: CourseListPanelProps) {
  return (
    <Card>
      <CardHeader className="flex flex-row items-center justify-between space-y-0">
        <div>
          <CardTitle className="text-lg">Courses</CardTitle>
          <CardDescription>Refresh courses, then pick one to explore.</CardDescription>
        </div>
        <Button size="sm" variant="outline" onClick={onRefresh} disabled={refreshing}>
          {refreshing ? "Refreshing…" : "Refresh"}
        </Button>
      </CardHeader>
      <CardContent>
        {error ? (
          <p className="text-sm text-destructive">{error}</p>
        ) : loading ? (
          <p className="text-sm text-muted-foreground">Loading courses…</p>
        ) : courses.length === 0 ? (
          <p className="text-sm text-muted-foreground">
            No courses yet. Click refresh after configuring Canvas credentials.
          </p>
        ) : (
          <ScrollArea className="h-[420px]">
            <div className="space-y-2">
              {courses.map((course) => (
                <button
                  key={course.id}
                  type="button"
                  onClick={() => onSelectCourse(course.id)}
                  className={cn(
                    "w-full rounded-md border px-3 py-2 text-left transition-colors hover:bg-accent",
                    selectedCourseId === course.id
                      ? "border-primary bg-accent"
                      : "border-transparent",
                  )}
                >
                  <div className="font-medium">{course.name}</div>
                  <div className="text-xs text-muted-foreground">
                    Last synced {formatDateTime(course.last_synced_at)}
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

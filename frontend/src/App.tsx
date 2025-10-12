import { useDashboardData } from "@/hooks/useDashboardData";
import { DashboardHeader } from "@/components/dashboard/DashboardHeader";
import { CourseListPanel } from "@/components/dashboard/CourseListPanel";
import { ModuleListPanel } from "@/components/dashboard/ModuleListPanel";
import { ItemPanel } from "@/components/dashboard/ItemPanel";
import { ItemDetailPanel } from "@/components/dashboard/ItemDetailPanel";

function App() {
  const {
    apiBaseUrl,
    healthStatus,
    healthError,
    actionMessage,
    courses,
    loadingCourses,
    coursesError,
    selectedCourseId,
    refreshingCourses,
    modules,
    loadingModules,
    modulesError,
    selectedModuleId,
    refreshingModules,
    items,
    loadingItems,
    itemsError,
    selectedItemId,
    filters,
    providerOptions,
    itemDetail,
    loadingDetail,
    detailError,
    actionBusy,
    refreshCourses,
    refreshModules,
    selectCourse,
    selectModule,
    selectItem,
    setSearch,
    setProvider,
    toggleStatus,
    resetFilters,
    queueTranscript,
    queueSummary,
  } = useDashboardData();

  const selectedCourse = courses.find((course) => course.id === selectedCourseId) ?? null;
  const selectedModule = modules.find((module) => module.id === selectedModuleId) ?? null;

  return (
    <div className="min-h-screen bg-background text-foreground">
      <DashboardHeader
        apiBaseUrl={apiBaseUrl}
        healthStatus={healthStatus}
        healthError={healthError}
        actionMessage={actionMessage}
      />
      <main className="container grid gap-6 py-6">
        <section className="grid gap-4 lg:grid-cols-[280px_320px_1fr]">
          <CourseListPanel
            courses={courses}
            selectedCourseId={selectedCourseId}
            onSelectCourse={selectCourse}
            loading={loadingCourses}
            error={coursesError}
            onRefresh={refreshCourses}
            refreshing={refreshingCourses}
          />
          <ModuleListPanel
            modules={modules}
            selectedModuleId={selectedModuleId}
            onSelectModule={selectModule}
            loading={loadingModules}
            error={modulesError}
            onRefresh={refreshModules}
            refreshing={refreshingModules}
            courseName={selectedCourse ? selectedCourse.name : null}
          />
          <ItemPanel
            items={items}
            selectedItemId={selectedItemId}
            onSelectItem={selectItem}
            loading={loadingItems}
            error={itemsError}
            filters={filters}
            onSearchChange={setSearch}
            onProviderChange={setProvider}
            onResetFilters={resetFilters}
            onToggleStatus={toggleStatus}
            providerOptions={providerOptions}
            selectedModuleTitle={selectedModule ? selectedModule.title : null}
          />
        </section>
        <section>
          <ItemDetailPanel
            itemDetail={itemDetail}
            loading={loadingDetail}
            error={detailError}
            actionBusy={actionBusy}
            apiBaseUrl={apiBaseUrl}
            onQueueTranscript={queueTranscript}
            onQueueSummary={queueSummary}
          />
        </section>
      </main>
    </div>
  );
}

export default App;

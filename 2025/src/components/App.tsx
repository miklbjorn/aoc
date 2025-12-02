'use client';

import { SelectedEventProvider } from "@/hooks/EventSelectionProvider";
import { EventDay } from "./EventDay";
import { SomeOtherComponent } from "./SomeOtherComponent";

export function App({year=undefined}: {year?: number}) {

    year = year ?? new Date().getFullYear();

    return (
        <SelectedEventProvider default_year={year}>
        <SomeOtherComponent />

        <EventDay />
        </SelectedEventProvider>
  );
}
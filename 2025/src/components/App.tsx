'use client';

import { useSelectedEvent, useSelectedEventDispatch } from "@/hooks/EventSelectionProvider";
import { EventDay } from "./EventDay";
import { SomeOtherComponent } from "./SomeOtherComponent";
import { useEffect } from "react";

export function App({year}: {year?: number}) {

  const dispatch = useSelectedEventDispatch();
  const event = useSelectedEvent();

  useEffect(() => {
    if (year && year !== event.year) {
      console.log("Setting year to", year);
      dispatch({ type: "set_year", year: year, day: 1 });
    }
  }, [year, dispatch, event.year]);

    return (
       <> 
        <SomeOtherComponent />
        <EventDay />
        </>
  );
}
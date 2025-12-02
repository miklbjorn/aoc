'use client'

import { useReducer } from "react";
import { createContext, useContext } from "react";

type Event = {
    year: number;
    day: number
}

const DEFAULT_EVENT: Event = { year: 2025, day: 1 };

type SelectEventAction = {
    type: "set_event" | "set_year" | "set_day";
    year: number;
    day: number;
}

export const SelectedEventContext = createContext(DEFAULT_EVENT);
export const SelectedEventDispatchContext = createContext((action: SelectEventAction) => {DEFAULT_EVENT});



export function SelectedEventReducer(selectedEvent: Event, action: SelectEventAction) {
    console.log("Reducing action:", action);
    switch (action.type) {
        case "set_event":
            return { year: action.year ?? selectedEvent.year, day: action.day ?? selectedEvent.day };
        case "set_year":
            return { ...selectedEvent, year: action.year };
        case "set_day":
            return { ...selectedEvent, day: action.day };
        default:
            return selectedEvent;
    }
}

export function SelectedEventProvider({default_year=2025, children}: {default_year: number; children: React.ReactNode}) {
    const [selectedEvent, dispatch] = useReducer(SelectedEventReducer, { year: default_year, day: 1 });

    return (
        <SelectedEventContext value={selectedEvent}>
            <SelectedEventDispatchContext value={dispatch}>
                {children}
            </SelectedEventDispatchContext>
        </SelectedEventContext>
    );
}

export function useSelectedEvent() {
    return useContext(SelectedEventContext);
}

export function useSelectedEventDispatch() {
    return useContext(SelectedEventDispatchContext);
}
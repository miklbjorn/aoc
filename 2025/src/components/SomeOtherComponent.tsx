import { useSelectedEvent } from "@/hooks/EventSelectionProvider";
import { use } from "react";

export function SomeOtherComponent() {
    const event = useSelectedEvent()

    return (
        <div>
            This is some other component. Showing the year: {event.year} and the day: {event.day}.
        </div>
    );
}
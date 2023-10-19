import React from "react";
import moment from "moment";

function EventGrid({
  currentWeek,
  selectedTimezone,
  events,
  setEvents,
  dayIndex,
}) {
  const weekStart = moment(currentWeek).startOf("week").add(dayIndex, "days");
  const isCurrentDate = moment(weekStart).isSameOrAfter(moment(), "day"); // Check if it's the current date
  const timeSlots = [];

  if (isCurrentDate) {
    for (let i = 9; i < 23; i++) {
      const time = moment(weekStart).add(i, "hours");
      timeSlots.push(time.format("LT"));
      timeSlots.push(time.add(30, "minutes").format("LT"));
    }
  }

  const handleEventCheckboxChange = (date, time) => {
    const dummyNames = [
      "John Doe",
      "Jane Smith",
      "David Johnson",
      "Mary Wilson",
      "Robert Lee",
      "Lisa Brown",
      "Michael Davis",
      "Jennifer Martinez",
      "William Anderson",
      "Sarah Thomas",
      "James Wilson",
      "Karen Garcia",
      "Joseph Taylor",
      "Nancy Hernandez",
      "Charles Gonzalez",
      "Patricia Lewis",
      "Daniel Hall",
      "Linda Scott",
      "Matthew Young",
      "Donna Clark",
    ];
    const eventIndex = events.findIndex(
      (event) => event.date === date && event.time === time
    );
    const newEvents = [...events];

    if (eventIndex !== -1) {
      newEvents.splice(eventIndex, 1);
    } else {
      const index = Math.floor(Math.random() * 20) + 1;
      newEvents.push({ name: dummyNames[index], date, time });
    }

    setEvents(newEvents);
  };

  return (
    <div>
      {!isCurrentDate&&<p>Past</p>}
      {timeSlots?.map((time) => {
        return (
          <div key={time} className="timeslots">
            <span>{time}</span>
            <input
              type="checkbox"
              onChange={() =>
                handleEventCheckboxChange(
                  moment(weekStart).format("YYYY-MM-DD"),
                  time
                )
              }
              checked={events.some(
                (event) =>
                  event.date === moment(weekStart).format("YYYY-MM-DD") &&
                  event.time === time
              )}
            />
          </div>
        );
      })}
    </div>
  );
}

export default EventGrid;

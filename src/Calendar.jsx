import React, { useEffect, useState } from "react";
import DateDisplay from "./DateDisplay";
import TimezoneSelect from "./TimezoneSelect";
import EventGrid from "./EventGrid";
import EventList from "./EventList";
import moment from "moment";
import momentTZ from "moment-timezone";
momentTZ.tz.setDefault("UTC");

function Calendar() {
  const [currentWeek, setCurrentWeek] = useState(moment());
  const [selectedTimezone, setSelectedTimezone] = useState("UTC-0");
  const [events, setEvents] = useState(
    JSON.parse(localStorage.getItem("events")) || []
  );
  const [datechange, setDatechange] = useState(currentWeek.date());

  const handlePreviousWeek = () => {
    setCurrentWeek((prevWeek) => prevWeek.subtract(7, "days"));
    setDatechange(currentWeek.date());
  };

  const handleNextWeek = () => {
    setCurrentWeek((nextWeek) => nextWeek.add(7, "days"));
    setDatechange(currentWeek.toDate());
  };

  const today = moment(); // Get today's date
  const weekStart = today.clone().startOf("week"); // Start from the beginning of the current week containing today
  const weekEnd = weekStart.clone().endOf("week");

  useEffect(() => {
    localStorage.setItem("events", JSON.stringify(events));
  }, [events]);

  useEffect(() => {
    // console.log("i am rendered");
  }, [datechange]);

  return (
    <div className="calendar">
      <h1>Calendar App</h1>
      <div>
        <button onClick={handlePreviousWeek}>Previous Week</button>
        <DateDisplay currentWeek={currentWeek.toDate()} />
        <button onClick={handleNextWeek}>Next Week</button>
      </div>
      <TimezoneSelect
        selectedTimezone={selectedTimezone}
        setSelectedTimezone={setSelectedTimezone}
      />
      <div>
        <table style={{ width: "100%" }}>
          <tbody>
            {Array.from({ length: 7 }).map((_, index) => {
              const day = currentWeek
                .clone()
                .startOf("week")
                .add(index, "days");
              return (
                <tr key={day.format("YYYY-MM-DD")}>
                  <th style={{ width: "20%" }}>
                    <h3>{day.format("dddd")}</h3>
                    <span>{day.format("MM/DD")}</span>
                  </th>
                  <td>
                    <EventGrid
                      currentWeek={currentWeek.toDate()}
                      selectedTimezone={selectedTimezone}
                      events={events}
                      setEvents={setEvents}
                      dayIndex={index}
                    />
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
      <EventList events={events} />
    </div>
  );
}

export default Calendar;

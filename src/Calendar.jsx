import React, { useEffect, useState } from "react";
import DateDisplay from "./DateDisplay";
import TimezoneSelect from "./TimezoneSelect";
import EventGrid from "./EventGrid";
import EventList from "./EventList";
import moment from "moment";
import momentTZ from "moment-timezone";
momentTZ.tz.setDefault("UTC");

const data = [
  {
    name: "Karen Garcia",
    date: "2023-10-20",
    time: "10:00 AM",
  },
  {
    name: "Joseph Taylor",
    date: "2023-10-20",
    time: "10:30 AM",
  },
  {
    name: "Daniel Hall",
    date: "2023-10-20",
    time: "10:30 PM",
  },
  {
    name: "Matthew Young",
    date: "2023-10-20",
    time: "5:30 PM",
  },
  {
    name: "James Wilson",
    date: "2023-10-21",
    time: "9:00 PM",
  },
  {
    name: "Matthew Young",
    date: "2023-10-21",
    time: "12:30 PM",
  },
  {
    name: "Robert Lee",
    date: "2023-10-21",
    time: "9:00 AM",
  },
  {
    name: "Daniel Hall",
    date: "2023-10-21",
    time: "10:30 AM",
  },
  {
    name: "Linda Scott",
    date: "2023-10-21",
    time: "6:30 PM",
  },
  {
    name: "Patricia Lewis",
    date: "2023-10-29",
    time: "9:30 AM",
  },
  {
    name: "Nancy Hernandez",
    date: "2023-10-29",
    time: "9:00 AM",
  },
  {
    name: "William Anderson",
    date: "2023-10-29",
    time: "10:00 PM",
  },
  {
    name: "Jennifer Martinez",
    date: "2023-10-30",
    time: "11:30 AM",
  },
  {
    name: "Karen Garcia",
    date: "2023-10-31",
    time: "10:00 AM",
  },
  {
    name: "Jane Smith",
    date: "2023-10-30",
    time: "2:00 PM",
  },
  {
    name: "Mary Wilson",
    date: "2023-10-30",
    time: "10:30 AM",
  },
  {
    name: "Linda Scott",
    date: "2023-11-01",
    time: "10:30 AM",
  },
  {
    name: "Nancy Hernandez",
    date: "2023-11-01",
    time: "11:30 AM",
  },
  {
    name: "Patricia Lewis",
    date: "2023-11-02",
    time: "11:30 AM",
  },
  {
    name: "Jane Smith",
    date: "2023-11-02",
    time: "10:00 AM",
  },
  {
    name: "Mary Wilson",
    date: "2023-11-02",
    time: "1:30 PM",
  },
  {
    name: "Karen Garcia",
    date: "2023-11-02",
    time: "2:00 PM",
  },
  {
    name: "Michael Davis",
    date: "2023-11-03",
    time: "10:00 AM",
  },
  {
    name: "Jane Smith",
    date: "2023-11-03",
    time: "3:00 PM",
  },
  {
    name: "Lisa Brown",
    date: "2023-11-04",
    time: "10:00 AM",
  },
  {
    name: "Patricia Lewis",
    date: "2023-11-04",
    time: "11:30 AM",
  },
  {
    name: "Donna Clark",
    date: "2023-11-04",
    time: "6:00 PM",
  },
  {
    name: "Nancy Hernandez",
    date: "2023-11-04",
    time: "5:00 PM",
  },
  {
    name: "Mary Wilson",
    date: "2023-11-03",
    time: "9:00 AM",
  },
  {
    name: "David Johnson",
    date: "2023-11-01",
    time: "4:30 PM",
  },
];

function Calendar() {
  const [currentWeek, setCurrentWeek] = useState(moment());
  const [selectedTimezone, setSelectedTimezone] = useState("UTC-0");
  const [events, setEvents] = useState(data);
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

import React from "react";

function EventList({ events }) {
  // You can map through the events and display them here.

  return (
    <div>
      <div>
        <h2>Events</h2>
      </div>
      <div>
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Name</th>
              <th>Date</th>
              <th>Time</th>
            </tr>
          </thead>
          <tbody>
            {events?.map((event, i) => {
              return (
                <tr key={i + 1}>
                  <td>{i + 1}</td>
                  <td>{event.name}</td>
                  <td>{event.date}</td>
                  <td>{event.time}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default EventList;

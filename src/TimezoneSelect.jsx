import React, { useState } from "react";
import momentTZ from "moment-timezone";

function TimezoneSelect({ selectedTimezone, setSelectedTimezone }) {
  const handleTimezoneChange = (e) => {
    const newTimezone = e.target.value;
    setSelectedTimezone(newTimezone);
    momentTZ.tz.setDefault(newTimezone);
  };

  return (
    <div className="timezone">
      <label>Timezone: </label>
      <select value={selectedTimezone} onChange={handleTimezoneChange}>
        <option value="UTC">UTC</option>
        <option value="America/New_York">Eastern Time</option>
        {/* Add more timezone options as needed */}
      </select>
    </div>
  );
}

export default TimezoneSelect;

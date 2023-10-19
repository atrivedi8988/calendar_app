import React from "react";
import moment from "moment";

function DateDisplay({ currentWeek }) {
  const currentDate = moment(new Date()).format("LL z");
  return <div className="date-display">{currentDate}</div>;
}

export default DateDisplay;

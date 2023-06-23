var now = new Date();
const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
var dotw = daysOfWeek[now.getDay()];
var y = now.getFullYear();
var m = now.getMonth();
var d = now.getDate();

function amTimes(am_open, am_close) {
  document.getElementById("vv-head").innerHTML = "THE POOL IS CURRENTLY <u>OPEN</u>:";
  document.getElementById("vv-body").innerHTML = "<u>Open Swim (ALL AGES)</u><br><b>" + am_open.toLocaleString('en-US', {
    hour: 'numeric',
    minute: 'numeric',
    hour12: true
  }) + " - " + am_close.toLocaleString('en-US', {
    hour: 'numeric',
    minute: 'numeric',
    hour12: true
  }) + "</b>";
}

function familyNight(family_night_open, family_night_close) {
  document.getElementById("vv-head").innerHTML = "THE POOL IS CURRENTLY <u>OPEN</u>:";
  document.getElementById("vv-body").innerHTML = "<u>Family Night - $15 per family (ALL AGES)</u><br><b>" + family_night_open.toLocaleString('en-US', {
    hour: 'numeric',
    minute: 'numeric',
    hour12: true
  }) + " - " + family_night_close.toLocaleString('en-US', {
    hour: 'numeric',
    minute: 'numeric',
    hour12: true
  }) + "</b>";
}

function halfOff(half_off_open, half_off_close) {
  document.getElementById("vv-head").innerHTML = "OPEN:";
  document.getElementById("vv-body").innerHTML = "<u>Open Swim - Half Price! (ALL AGES)</u><br><b>" + half_off_open.toLocaleString('en-US', {
    hour: 'numeric',
    minute: 'numeric',
    hour12: true
  }) + " - " + half_off_close.toLocaleString('en-US', {
    hour: 'numeric',
    minute: 'numeric',
    hour12: true
  }) + "</b>";
}

function morning(am_open) {
  document.getElementById("vv-head").innerHTML = "THE POOL IS CURRENTLY <u>CLOSED</u>";
  document.getElementById("vv-body").innerHTML = "We will be open at " + am_open.toLocaleString('en-US', {
    hour: 'numeric',
    minute: 'numeric',
    hour12: true
  });
}

var am_open = new Date(y, m, d, 12, 0);
if (dotw === "Saturday") {
  var am_close = new Date(y, m, d, 18, 0);
  if (am_open <= now && now < am_close) {
    amTimes(am_open, am_close);
  } else if (am_close <= now) {
    document.getElementById("vv-head").innerHTML = "THE POOL IS CURRENTLY <u>CLOSED</u>";
  } else if (now < am_open) {
    morning(am_open);
  }
} else {
  var am_close = new Date(y, m, d, 17, 30);
  var adult_swim_open = new Date(y, m, d, 17, 30);
  var adult_swim_close = new Date(y, m, d, 18, 30);
  var pm_open = new Date(y, m, d, 18, 30);
  var pm_close = new Date(y, m, d, 20, 30);
  if (am_open <= now && now < am_close) {
    amTimes(am_open, am_close);
  } else if (adult_swim_open <= now && now < adult_swim_close) {
    document.getElementById("vv-head").innerHTML = "THE POOL IS CURRENTLY <u>OPEN</u>:";
    document.getElementById("vv-body").innerHTML = "<u>Current Walking and Adult Lap Swim (18+ ONLY)</u><br><b>" + adult_swim_open.toLocaleString('en-US', {
    hour: 'numeric',
    minute: 'numeric',
    hour12: true
  }) + " - " + adult_swim_close.toLocaleString('en-US', {
    hour: 'numeric',
    minute: 'numeric',
    hour12: true
  }) + "</b>";
  } else if (pm_open <= now && now < pm_close) {
    if (dotw === "Wednesday" || dotw === "Sunday") {
      familyNight(pm_open, pm_close);
    } else {
      halfOff(pm_open, pm_close);
    }
  } else if (pm_close <= now) {
    document.getElementById("vv-head").innerHTML = "THE POOL IS CURRENTLY <u>CLOSED</u>";
  } else if (now < am_open) {
    morning(am_open);
  }
}
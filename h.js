var now = new Date();
var dotw = now.toLocaleString('en-us', { weekday: 'long' });
var y = now.getFullYear();
var m = now.getMonth();
var d = now.getDate();

function swimLessons() {
  const sl1 = new Date(2023, 5, 5) <= now && now < new Date(2023, 5, 9);
  const sl2 = new Date(2023, 5, 12) <= now && now < new Date(2023, 5, 16);
  const sl3 = new Date(2023, 5, 19) <= now && now < new Date(2023, 5, 23);
  const sl4 = new Date(2023, 5, 26) <= now && now < new Date(2023, 5, 30);
  const sl5 = new Date(2023, 6, 10) <= now && now < new Date(2023, 6, 14);
  const sl6 = new Date(2023, 6, 17) <= now && now < new Date(2023, 6, 21);
  const sl7 = new Date(2023, 6, 24) <= now && now < new Date(2023, 6, 28);
  const sl8 = new Date(2023, 6, 31) <= now && now < new Date(2023, 7, 4);
  if (sl1 || sl2 || sl3 || sl4 || sl5 || sl6 || sl7 || sl8) {
    return true;
  }
}

function amTimes(am_open, am_close) {
    document.getElementById("h-head").innerHTML = "THE POOL IS CURRENTLY <u>OPEN</u>:";
    document.getElementById("h-body").innerHTML = "<u>Open Swim (ALL AGES)</u><br><b>" + am_open.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true }) + " - " + am_close.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true }) + "</b>";
}

function familyNight(family_night_open, family_night_close) {
    document.getElementById("h-head").innerHTML = "THE POOL IS CURRENTLY <u>OPEN</u>:";
    document.getElementById("h-body").innerHTML = "<u>Family Night - $15 per family (ALL AGES)</u><br><b>"+ family_night_open.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true }) + " - " + family_night_close.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true }) + "</b>";
}

function halfOff(half_off_open, half_off_close) {
    document.getElementById("h-head").innerHTML = "THE POOL IS CURRENTLY <u>OPEN</u>:";
    document.getElementById("h-body").innerHTML = "<u>Open Swim - Half Price! (ALL AGES)</u><br><b>" + half_off_open.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true }) + " - " + half_off_close.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true }) + "</b>";
}

function morning(am_open) {
  document.getElementById("h-head").innerHTML = "THE POOL IS CURRENTLY <u>CLOSED</u>";
  document.getElementById("h-body").innerHTML = "We will be open at " + am_open.toLocaleString('en-US', {
    hour: 'numeric',
    minute: 'numeric',
    hour12: true
  });
}

if (new Date(2023, 5, 2) <= now && now < new Date(2023, 8, 1)) {
  if (dotw === "Sunday") {
    var am_open = new Date(y, m, d, 12, 0);
    var am_close = new Date(y, m, d, 17, 45);
    var family_night_open = new Date(y, m, d, 18, 30);
    var family_night_close = new Date(y, m, d, 20, 30);
    if (am_open <= now && now < am_close) {
      amTimes(am_open, am_close);
    } else if (am_close <= now && now < family_night_open) {
        document.getElementById("h-head").innerHTML = "THE POOL IS CURRENTLY <u>CLOSED</u>";
        document.getElementById("h-body").innerHTML = "Family Night starts at 6:30 PM";
    } else if (family_night_open <= now && now < family_night_close) {
      familyNight(family_night_open, family_night_close);
    } else if (family_night_close <= now) {
        document.getElementById("h-head").innerHTML = "THE POOL IS CURRENTLY <u>CLOSED</u>";
    } else if (now < am_open) {
      morning(am_open);
    }
  } else if (dotw === "Saturday") {
    var am_open = new Date(y, m, d, 11, 30);
    var am_close = new Date(y, m, d, 18, 0);
    if (am_open <= now && now < am_close) {
      amTimes(am_open, am_close);
    } else if (am_close <= now) {
        document.getElementById("h-head").innerHTML = "THE POOL IS CURRENTLY <u>CLOSED</u>";
    } else if (now < am_open) {
      morning(am_open);
    }
  } else if (dotw === "Monday" || dotw === "Tuesday" || dotw === "Thursday") {
    var am_open = new Date(y, m, d, 11, 30);
    if (swimLessons()) {
      var am_close = new Date(y, m, d, 17, 30);
      if (am_open <= now && now < am_close) {
        amTimes(am_open, am_close);
      } else if (am_close <= now) {
        document.getElementById("h-head").innerHTML = "THE POOL IS CURRENTLY <u>CLOSED</u>";
      } else if (now < am_open) {
        morning(am_open);
      }
    } else {
      var am_close = new Date(y, m - 1, d, 19, 0);
      var half_off_open = new Date(y, m - 1, d, 17, 0);
      var half_off_close = new Date(y, m - 1, d, 19, 0);
      if (am_open <= now && now < am_close) {
        amTimes(am_open, am_close);
      } else if (half_off_open <= now && now < half_off_close) {
        halfOff(half_off_open, half_off_close);
      } else if (half_off_close <= now) {
        document.getElementById("h-head").innerHTML = "THE POOL IS CURRENTLY <u>CLOSED</u>";
      } else if (now < am_open) {
        morning(am_open);
      }
    }
  } else if (dotw === "Friday") {
    var am_open = new Date(y, m, d, 11, 30);
    var am_close = new Date(y, m, d, 19, 0);
    var half_off_open = new Date(y, m, d, 17, 0);
    var half_off_close = new Date(y, m, d, 19, 0);
    if (am_open <= now && now < am_close) {
      amTimes(am_open, am_close);
    } else if (half_off_open <= now && now < half_off_close) {
      halfOff(half_off_open, half_off_close);
    } else if (half_off_close <= now) {
        document.getElementById("h-head").innerHTML = "THE POOL IS CURRENTLY <u>CLOSED</u>";
    } else if (now < am_open) {
      morning(am_open);
    }
  } else if (dotw === "Wednesday") {
    var am_open = new Date(y, m, d, 11, 30);
    if (swimLessons()) {
      var am_close = new Date(y, m, d, 17, 30);
      if (am_open <= now && now < am_close) {
        amTimes(am_open, am_close);
      } else if (am_close <= now) {
        document.getElementById("h-head").innerHTML = "THE POOL IS CURRENTLY <u>CLOSED</u>";
      } else if (now < am_open) {
        morning(am_open);
      }
    } else {
      var am_close = new Date(y, m, d, 17, 45);
      var family_night_open = new Date(y, m, d, 18, 30);
      var family_night_close = new Date(y, m, d, 20, 30);
      if (am_open <= now && now < am_close) {
        amTimes(am_open, am_close);
      } else if (am_close <= now && now < family_night_open) {
        document.getElementById("h-head").innerHTML = "THE POOL IS CURRENTLY <u>CLOSED</u>";
        document.getElementById("h-body").innerHTML = "Family Night starts at 6:30 PM";
      } else if (family_night_open <= now && now < family_night_close) {
        familyNight(family_night_open, family_night_close);
      } else if (family_night_close <= now) {
        document.getElementById("h-head").innerHTML = "THE POOL IS CURRENTLY <u>CLOSED</u>";
      } else if (now < am_open) {
        morning(am_open);
      }
    }
  }
}
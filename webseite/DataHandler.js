let input = document.querySelector("input");

input.onchange = e => {
  /**
  * ausgewählte Datei speichern
  */
  var file = e.target.files[0];

  /**
  * Reader laden & Inhalt laden
  */
  var reader = new FileReader();
  reader.readAsText(file, 'UTF-8');

  /**
  * Inhalt der Datei in Variable speichern
  */
  reader.onload = readerEvent => {
    var content = readerEvent.target.result;
    processData(content);
  }
}

// input.click();

/**
 * Listen mit den Werten für das Diagramm
 */
var labelDate = [];
var spannungA = [];
var spannungB = [];

/**
 * allTextLines: Array mit den Zeilen der csv Datei
 * lines: 2d Array -> zeilen und Zeilenterme
 */
var lines = [];
var allTextLines;

function processData(allText) {
  /**
   * allTextLines wird mit csv Inhalt gefüllt und editiert
   */
  allTextLines = allText.split(/\r\n|\n/);

  /**
   * erstellung 2d Array
   */
  for (var i = 0; i < allTextLines.length - 1; i++) {
    if(!allTextLines[i].length == 0){
      lines.push(allTextLines[i].split(','));
    }
  }
  // console.log(allTextLines);
  // console.log("----------");
  // console.log(lines);

  /**
   * Datenzeilen werden den Wertelisten hinzugefügt
   */
  for (var i = 0; i < lines.length - 1; i++) {
    var h = lines[i][0];
    h = h.replace('"', '');
    h = h.replace('"', '');
    labelDate.push(h);
  }

  for (var i = 0; i < lines.length - 1; i++) {
    var h = lines[i][1];
    h = h.replace('"', '');
    h = h.replace('"', '');
    spannungA.push(h);
  }

  for (var i = 0; i < lines.length - 1; i++) {
    var h = lines[i][2];
    h = h.replace('"', '');
    h = h.replace('"', '');
    spannungB.push(h);
  }

  /**
   * Diagramm laden
   */
  var ctx = document.getElementById("myChart").getContext('2d');
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labelDate,
      datasets: [{
        label: ['feste SolarPlatte'],
        data: spannungA,
        backgroundColor: [
          'rgba(0, 0, 0, 0)'
        ],
        borderColor: [
          'rgba(192,22,22,1)'
        ],
        borderWidth: 1
      }, {
        label: ['bewegliche SolarPlatte'],
        data: spannungB,
        backgroundColor: [
          'rgba(0, 0, 0, 0)'
        ],
        borderColor: [
          'rgba(22,193,195,1)'
        ],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: true
          },
          scaleLabel: {
            display: true,
            labelString: 'U (V)',
            fontSize: 20
          }
        }]
      },
      elements: {
        line: {
          tension: 0
        }
      }
    }
  });
}

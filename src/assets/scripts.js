var isVis1EventSet = false;
var isVis2EventSet = false;
var isVis3EventSet = false;

document.body.addEventListener('DOMNodeInserted', function( event ) {
    let myPlot1 = document.getElementById("viz1-graph")
    if (myPlot1 === null){ return; }
    if (myPlot1.children[1] === undefined){ return; }
    if (myPlot1.children[1].on === undefined){ return; }

    if(!isVis1EventSet) {
        myPlot1.children[1].on('plotly_hover', function (eventdata) {
            console.log(eventdata)
            let hovered = eventdata.points[0]

            let cn = hovered.customdata[1];
            let pn = hovered.customdata[2];

            console.log({cn: cn, pn: pn})
            Plotly.Fx.hover(myPlot1.children[1], [
                {curveNumber: hovered.curveNumber, pointNumber: hovered.pointNumber},
                {curveNumber: cn, pointNumber: pn},
            ], ['xy', 'x2y2']);
        })
        isVis1EventSet = true;
    }

    let myPlot2 = document.getElementById("viz2-graph")
    if (myPlot2 === null){ return; }
    if (myPlot2.children[1] === undefined){ return; }
    if (myPlot2.children[1].on === undefined){ return; }

    if(!isVis2EventSet) {
        myPlot2.children[1].on('plotly_hover', function (eventdata) {
            console.log(eventdata)
            let hovered = eventdata.points[0]

            let cn = hovered.customdata[1];
            let pn = hovered.customdata[2];

            console.log({cn: cn, pn: pn})
            Plotly.Fx.hover(myPlot2.children[1], [
                {curveNumber: hovered.curveNumber, pointNumber: hovered.pointNumber},
                {curveNumber: cn, pointNumber: pn},
            ], ['xy', 'x2y2']);
        })
        isVis2EventSet = true;
    }

    let myPlot3 = document.getElementById("viz3-graph");
    if (myPlot3 === null){ return; }
    if (myPlot3.children[1] === undefined){ return; }
    if (myPlot3.children[1].on === undefined){ return; }

    if(!isVis3EventSet) {
        myPlot3.children[1].on('plotly_hover', function (eventdata) {
            console.log(eventdata)
            let hovered = eventdata.points[0]

            let cn;
            if (hovered.curveNumber > 8) {
                cn = hovered.curveNumber - 9
            } else {
                cn = hovered.curveNumber + 9
            }

            console.log({cn: hovered.curveNumber + 9, pn: hovered.pointNumber})
            Plotly.Fx.hover(myPlot3.children[1], [
                {curveNumber: hovered.curveNumber, pointNumber: hovered.pointNumber},
                {curveNumber: cn, pointNumber: hovered.pointNumber},
            ], ['xy', 'x2y2']);
        })
        isVis3EventSet = true;
    }
}, false);

var isEventSet = false;
document.body.addEventListener('DOMNodeInserted', function( event ) {
    let myPlot1 = document.getElementById("viz1-1")
    if (myPlot1 === null){ return; }
    if (myPlot1.children[1] === undefined){ return; }
    if (myPlot1.children[1].on === undefined){ return; }

    if(isEventSet){ return; }

    myPlot1.children[1].on('plotly_hover', function (eventdata){
        console.log(eventdata)
        let hovered = eventdata.points[0]

        let cn;
        let pn = hovered.customdata[2];
        if(hovered.curveNumber > 3) { cn = hovered.customdata[1]}
        else { cn = hovered.customdata[1] + 4 }

        console.log({cn:cn, pn:pn})
        //Plotly.Fx.hover('js-v-11', [{curveNumber: 4, pointIndex:28},]);
        Plotly.Fx.hover(myPlot1.children[1], [
            {curveNumber:hovered.curveNumber, pointNumber:hovered.pointNumber},
            {curveNumber:cn, pointNumber:pn},
        ], ['xy', 'x2y2']);
    })
    isEventSet = true;
}, false);

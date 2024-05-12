
function updateGraph(year) {
    
    const graphData = getGraphData(year); 
    const graphImage = generateGraphImage(graphData); 
    document.getElementById("graph-image").src = graphImage; 
  }
  
  document.getElementById("year-2019").addEventListener("click", function() {
    updateGraph(2019);
  });
  
  document.getElementById("year-2020").addEventListener("click", function() {
    updateGraph(2020);
  });
  
 
  updateGraph(2019); 
  
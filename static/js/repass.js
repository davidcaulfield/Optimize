(function(window, location) {
//     // history.replaceState(null, document.title, location.pathname+"/analyzed");
//     history.replaceState(null, document.title, location.replace("http://127.0.0.1/analyzed"));
//     history.pushState(null, document.title, location.pathname);
//     console.log("getting here")
//     window.addEventListener("popstate", function() {
//       if(location.hash === "/stock-info") {
//             history.replaceState(null, document.title, location.pathname);
//             setTimeout(function(){
//               location.replace("http://127.0.0.1/");
//             },0);
//       }
//     }, false);
console.log( window.location.href );
window.history.replaceState( {} , 'analyzed_home', '/analyzed_home' );
console.log( window.location.href );
}(window, location));




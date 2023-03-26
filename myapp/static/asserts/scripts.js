
//buildList()
//
//function buildList(){
//  var wrapper = document.getElementById('list-wrapper')
//  var url='http://127.0.0.1:8000/get_task/'
//
//  fetch(url)
//  .then((respn) => respn.json())
//  .then(function(data){
//   console.log(data)
//
//   var list = data-->
//   for (var i in list){
//
//
////<!--					try{-->
////<!--						document.getElementById(`data-row-${i}`).remove()-->
////<!--					}catch(err){-->
////
////<!--					}-->
////
////
////
////<!--					var title = `<span class="title">${list[i].title}</span>`
////<!--					if (list[i].completed == true){-->
////<!--						title = `<strike class="title">${list[i].title}</strike>`
////					}
//
//					var item = `
//
//						<div style="flex:7">
//								${title}
//						</div>
//
//					`
//					wrapper.innerHTML += item
//
//			}
//
//  });
//
//}
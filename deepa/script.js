const API = "http://127.0.0.1:8000/blogs";



// CREATE BLOG

function createBlog(){

    let title =
    document.getElementById("title").value;


    let content =
    document.getElementById("content").value;



    fetch(API,{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            title:title,
            content:content

        })

    })

    .then(response=>response.json())

    .then(()=>{

        loadBlogs();

        document.getElementById("title").value="";

        document.getElementById("content").value="";

    });

}




// READ BLOGS

function loadBlogs(){


fetch(API)

.then(response=>response.json())

.then(data=>{


let output="";


data.forEach(blog=>{


output += `


<div class="blog-card">


<h3>${blog.title}</h3>


<p>${blog.content}</p>



<button class="update"
onclick="updateBlog(${blog.id})">

Update

</button>



<button class="delete"
onclick="deleteBlog(${blog.id})">

Delete

</button>


</div>


`;

});


document.getElementById("blogs").innerHTML=output;


});


}





// UPDATE BLOG

function updateBlog(id){


let title = prompt("Enter new title");

let content = prompt("Enter new content");



fetch(`${API}/${id}`,{

method:"PUT",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

title:title,

content:content

})


})

.then(()=>loadBlogs());


}





// DELETE BLOG

function deleteBlog(id){


fetch(`${API}/${id}`,{

method:"DELETE"

})

.then(()=>loadBlogs());


}



loadBlogs();
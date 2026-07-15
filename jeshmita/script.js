const API_URL = "http://127.0.0.1:8000/blogs";

let editId = null;


// Load blogs when page opens
window.onload = function () {

    loadBlogs();

};




// CREATE / UPDATE BLOG

async function saveBlog() {


    let title = document.getElementById("title").value.trim();

    let content = document.getElementById("content").value.trim();



    if(title === "" || content === ""){

        alert("Please enter title and content");

        return;

    }



    let blog = {

        title: title,

        content: content

    };





    try {


        if(editId === null){


            // CREATE

            await fetch(API_URL, {

                method:"POST",

                headers:{

                    "Content-Type":"application/json"

                },

                body:JSON.stringify(blog)

            });


        }

        else{


            // UPDATE

            await fetch(`${API_URL}/${editId}`, {

                method:"PUT",

                headers:{

                    "Content-Type":"application/json"

                },

                body:JSON.stringify(blog)

            });



            editId = null;


        }





        document.getElementById("title").value = "";

        document.getElementById("content").value = "";



        loadBlogs();



    }

    catch(error){

        console.log(error);

        alert("FastAPI server is not running");

    }



}









// READ ALL BLOGS


async function loadBlogs(){



    try{


        let response = await fetch(API_URL);


        let blogs = await response.json();



        let output = "";




        blogs.forEach(blog => {



            output += `


            <div class="blog-post">


                <h3>${blog.title}</h3>


                <p>${blog.content}</p>



                <button onclick="editBlog(${blog.id})">

                    Edit

                </button>




                <button onclick="deleteBlog(${blog.id})">

                    Delete

                </button>



            </div>


            `;



        });





        document.getElementById("blogs").innerHTML = output;



    }


    catch(error){


        console.log(error);


        document.getElementById("blogs").innerHTML =
        "<p>Unable to load blogs</p>";

    }



}









// EDIT BLOG


async function editBlog(id){



    let response = await fetch(`${API_URL}/${id}`);


    let blog = await response.json();





    document.getElementById("title").value = blog.title;


    document.getElementById("content").value = blog.content;



    editId = id;




    window.scrollTo({

        top:document.getElementById("blog").offsetTop,

        behavior:"smooth"

    });



}









// DELETE BLOG


async function deleteBlog(id){



    let confirmDelete = confirm(

        "Are you sure you want to delete this blog?"

    );




    if(confirmDelete){



        await fetch(`${API_URL}/${id}`,{


            method:"DELETE"


        });



        loadBlogs();



    }



}
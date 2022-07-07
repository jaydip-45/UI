var mongoose=require('mongoose');
var ibook=mongoose.Schema({
    name:String
    price:Number
})
module.exports=mongoose.model("books",ibook)

//indexe.js

var express=require('express');
var bodyparser=require('body-parser');
var router=require('./route')
var mongoose=require('mongoose');

mongoose.connect("connectoionstrin").then(()=>{
    console.log('db connect')

    app=express()
    app.use{bodyparser.urlencoded({extended:false})};
    app.use(express.json())
    app.use('/api',router)

    app.listen(2000,()=>{
        console.log('server started')

    })
}).catch((err)=>{
    console.log(err);
})


///route.js

var express=require('express');
var router=express.Router();
var book=require('./Model/Book');

router.get("/book",ayanc(req,res)=>{
    const ibook= await book.find()
    res.send(Book)
})


///bok and service in angular project



///book.html...

<tr *ngFor="let i of books">
<td>{{i.name}}</td>
</tr>
///book.component.ts

books:any=[];
p=1;
key='id';



ngOnIint()

{
    this._BookService.getPost().subscribe((data:any)=>{
        console.log(data);
        this.book=data
    })
}
import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { IPost } from '../shared/models/models';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit {

  public posts: IPost[] = [];
  public loading = false;
  public name: any = '';
  public body: any ="";
  public logged = false;

  public login: any ='';
  public password: any='';

  // public tasks: Task[] = [];

  constructor(private provider: ProviderService) { }

  ngOnInit() {

    const token = localStorage.getItem('token');
    if(token){
      this.logged = true;
    }

    if(this.logged){
      this.provider.getPostList().then(res=>{
        this.posts = res;
        this.loading = true;
      });
    }
  }

  // getTasks(task_lists: TaskList){
  //   this.provider.getTasks(task_lists).then(res=>{
  //     this.tasks = res;
  //   })
  // }

  createPost(){
    if(this.name !== ''){
      this.provider.createPost(this.name, this.body).then(res=>{
        this.name = '';
        this.posts.push(res);
      });
    }
  }

  updatePost(p: IPost){
    this.provider.updatePost(p).then(res=>{
      console.log(p.title + 'has been updated!');
    })
  }

  // deleteTaskList(tl: TaskList){
  //   this.provider.deleteTaskList(tl.id).then(res=>{
  //     console.log(tl.name + 'has been deleted!');
  //     this.provider.getTaskLists().then(r =>{
  //       this.task_lists = r;
  //     });
  //   });
  // }

  auth(){
    if(this.login !== '' && this.password !==''){
      this.provider.auth(this.login,this.password).then(res=>{
        localStorage.setItem('token',res.token);

        this.logged = true;

        this.provider.getPostList().then(r=>{
          this.posts= r;
          this.loading = true;
        });

      });
    }
  }

  logout(){
    this.provider.logout().then(res=>{
      localStorage.clear();
      this.logged = false;
    });
  }

}

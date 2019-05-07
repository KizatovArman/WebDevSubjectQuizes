import { Injectable, EventEmitter } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';
import { IPost, IAuthResponse } from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService{
  
  public sendMessage = new EventEmitter<string>();

  constructor(http: HttpClient) { 
    super(http);
  }

  getPostList(): Promise<IPost[]> {
    return this.get('http://localhost:8000/api/posts/',{});
  }

  createPost(title: any, body: any): Promise<IPost> {
    return this.post('http://localhost:8000/api/posts/',{
      title: title,
      body: body
    });
  }
  
  updateTaskList(post: IPost): Promise<IPost>{
    return this.put(,{
     title: post.title,
     body: post.body
    });
  }

  auth(login: any, password: any): Promise<IAuthResponse>{
    return this.post('http://localhost:8000/api/login/',{
      username: login,
      password: password
    });
  }

  logout():Promise<any>{
    return this.post('http://localhost:8000/api/logout/',{

    });
  }

}

import { Injectable } from '@angular/core';
import { Http } from "@angular/http";

@Injectable()
export class TweetService {
  
  url = "http://localhost:3000";
  constructor(private http: Http) { }

  getData() {
    return this.http.get(this.url+"/api/hashtags");
}

}
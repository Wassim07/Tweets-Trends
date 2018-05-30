import { Injectable } from '@angular/core';
import { AngularFireDatabase, AngularFireList } from 'angularfire2/database'

@Injectable()
export class TweetService {
  
  tweetList: AngularFireList<any>;
  
  constructor(private firebase :AngularFireDatabase ) { }

  getData(){
    this.tweetList = this.firebase.list('tweets_counts');
    return this.tweetList;
  }
}
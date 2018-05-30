import { Component, OnInit } from '@angular/core';
import { TweetService } from '../services/tweet.service';

@Component({
  selector: 'app-hashtags-list',
  templateUrl: './hashtags-list.component.html',
  styleUrls: ['./hashtags-list.component.css']
})
export class HashtagsListComponent implements OnInit {

  data: Array<number>;
  labels: Array<string>;
  hashtags = [];

  show: boolean = false;

  constructor(private tweetService: TweetService) {

    this.labels = ['#AI', '#AR', '#MachineLearning', '#DeepLearning', '#BigData', '#VR', '#DevOps'];
    this.data = [0, 0, 0, 0, 0, 0, 0];
  }

  ngOnInit() {
    var value;
    var id;

    var data = this.tweetService.getData()
      .subscribe(response => {

        this.hashtags = response.json();
        console.log(this.hashtags)

        this.hashtags.forEach(element => {
          value = parseInt(element["value"]);
          id = this.filteringHashtags(element["_id"]);
          this.data[this.labels.indexOf(id)] += value;
        });
      })
  }




  getEntries() {
    return Array.from(this.hashtags.entries());
  }

  filteringHashtags(hashtag) {

    switch (hashtag) {

      case "#BigData": hashtag = "#BigData"; break;

      case "#AI": ;
      case "#ArtificialIntelligence": hashtag = "#AI"; break;

      case "#AR": ;
      case "#AugmentedReality": hashtag = "#AR"; break;

      case "#VR": ;
      case "#VirtualReality": hashtag = "#VR"; break;

      case "#ML": ;
      case "#MachineLearning": hashtag = "#MachineLearning"; break;

      case "#DL": ;
      case "#DeepLearning": hashtag = "#DeepLearning"; break;

      case "#DevOps": hashtag = "#DevOps"; break;
    }
    return hashtag;
  }

  showCharts() {
    this.show = !this.show;
  }
}
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

  newData = [0,0,0,0,0,0,0];
  show: boolean = false;

  hashtags: Map<string, number>;

  constructor(private tweetService: TweetService) {
    
    this.labels = ['#AI', '#AR', '#MachineLearning', '#DeepLearning', '#BigData', '#VR', '#DevOps'];
    this.data = [0, 0, 0, 0, 0, 0, 0];
    this.hashtags = new Map<string, number>();
    this.hashtags.set("#AI", 0);
    this.hashtags.set("#AR", 0);
    this.hashtags.set("#MachineLearning", 0);
    this.hashtags.set("#DeepLearning", 0);
    this.hashtags.set("#BigData", 0);
    this.hashtags.set("#VR", 0);
    this.hashtags.set("#DevOps", 0);

  }

  ngOnInit() {
    var old = 0;
    var data = this.tweetService.getData();
    data.snapshotChanges().subscribe(item => {
      item.forEach(element => {
        var payload_json = element.payload.toJSON();

        Object.values(payload_json).forEach(element => {

          //console.log(element[0]);
          element[0] = this.filteringHashtags(element[0]);

          if (this.hashtags.get(element[0]) == null) {
            this.hashtags.set(element[0], element[1]);
          }
          else {
            old = this.hashtags.get(element[0])
            this.hashtags.set(element[0], old += element[1]);
          }
        })
      });

      this.updateLabelsAndData();

    });
  }


  updateLabelsAndData() {
    var i = 0;
    for (let entry of Array.from(this.hashtags.entries())) {
      this.newData[i] = entry[1];
      i++;
    }
    this.data = Array.from(this.newData);
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
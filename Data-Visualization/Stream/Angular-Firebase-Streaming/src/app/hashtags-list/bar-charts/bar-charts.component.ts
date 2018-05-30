import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'bar-charts',
  templateUrl: './bar-charts.component.html',
  styleUrls: ['./bar-charts.component.css']
})
export class BarChartsComponent implements OnInit {

  @Input()
  data: Array<number> = [];
  @Input()
  labels: Array<string> = [];



  constructor() {
    console.log('hahahaha');


  }

  ngOnInit() {
    // for (let entry of Array.from(this.hashtags.entries())) {
    //   this.labels = [...this.labels, entry[0]];
    //   this.data = [...this.data, entry[1]];
    // }
  }


  getValue() {
    //console.log(this.labels.length);
    // this.labels.forEach(element => {
    //   console.log(element);

    // });

    console.log(this.data.length);
    this.data.forEach(element => {
      console.log(element);

    });
  }

}
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

  constructor() {}

  ngOnInit() {
  }
}
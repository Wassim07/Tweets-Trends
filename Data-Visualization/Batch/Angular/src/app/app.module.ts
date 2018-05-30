import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { environment } from '../environments/environment';
import { ReactiveFormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { HashtagsListComponent } from './hashtags-list/hashtags-list.component';
import { TweetService } from './services/tweet.service';
import { AngularFireDatabaseModule } from 'angularfire2/database';
import { AngularFireModule } from 'angularfire2';
import { AngularFirestoreModule } from 'angularfire2/firestore';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ChartsModule } from 'ng2-charts';
import { ChartsComponent } from './hashtags-list/charts/charts.component';
import { HttpModule } from '@angular/http';
import { BarChartsComponent } from './hashtags-list/bar-charts/bar-charts.component';



@NgModule({
  declarations: [
    AppComponent,
    HashtagsListComponent,
    DashboardComponent,
    ChartsComponent,
    BarChartsComponent,
  ],
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    FormsModule,
    HttpModule,
    ChartsModule
  ],
  providers: [ TweetService ],
  bootstrap: [AppComponent]
})
export class AppModule { }

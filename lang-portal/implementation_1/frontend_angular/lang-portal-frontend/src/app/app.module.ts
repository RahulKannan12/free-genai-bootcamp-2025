import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { MatButtonModule } from '@angular/material/button';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { SideNavComponent } from './components/side-nav/side-nav.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { StudyActivitiesIndexComponent } from './components/study-activities-index/study-activities-index.component';
import { WordsIndexComponent } from './components/words-index/words-index.component';
import { WordGroupsIndexComponent } from './components/word-groups-index/word-groups-index.component';
import { StudySessionsIndexComponent } from './components/study-sessions-index/study-sessions-index.component';
import { SettingsComponent } from './components/settings/settings.component';

const routes: Routes = [
  { path: 'dashboard', component: DashboardComponent },
  { path: 'study_activities', component: StudyActivitiesIndexComponent },
  { path: 'words', component: WordsIndexComponent },
  { path: 'groups', component: WordGroupsIndexComponent },
  { path: 'study_sessions', component: StudySessionsIndexComponent },
  { path: 'settings', component: SettingsComponent },
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' }
];

@NgModule({
  declarations: [
    AppComponent,
    SideNavComponent,
    DashboardComponent,
    StudyActivitiesIndexComponent,
    WordsIndexComponent,
    WordGroupsIndexComponent,
    StudySessionsIndexComponent,
    SettingsComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatSidenavModule,
    MatListModule,
    MatButtonModule,
    RouterModule.forRoot(routes)
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
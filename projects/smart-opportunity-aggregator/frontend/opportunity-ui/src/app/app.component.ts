import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OpportunityService } from './services/opportunity.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],  // ✅ Required for *ngFor
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  jobs: any[] = [];
  courses: any[] = [];

  constructor(private opportunityService: OpportunityService) { }

  ngOnInit() {
    this.loadJobs();
    this.loadCourses();
  }

  loadJobs() {
    this.opportunityService.getJobs().subscribe(data => {
      this.jobs = data;
    });
  }

  loadCourses() {
    this.opportunityService.getCourses().subscribe(data => {
      this.courses = data;
    });
  }

  scrapeJobs() {
    this.opportunityService.scrapeJobs().subscribe(() => {
      this.loadJobs();  // refresh data after POST
    });
  }

  scrapeCourses() {
    this.opportunityService.scrapeCourses().subscribe(() => {
      this.loadCourses();  // refresh data after POST
    });
  }

}

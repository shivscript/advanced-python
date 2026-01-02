import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class OpportunityService {

  private baseUrl = environment.apiUrl;

  constructor(private http: HttpClient) { }

  // GET requests
  getJobs() {
    return this.http.get<any[]>(`${this.baseUrl}/jobs`);
  }

  getCourses() {
    return this.http.get<any[]>(`${this.baseUrl}/courses`);
  }

  // POST requests
  scrapeJobs() {
    return this.http.post(`${this.baseUrl}/jobs/scrape`, {});
  }

  scrapeCourses() {
    return this.http.post(`${this.baseUrl}/courses/scrape`, {});
  }
}

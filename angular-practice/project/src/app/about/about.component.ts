import { Component } from '@angular/core';
import { HomepageComponent } from '../homepage/homepage.component';
import { RouterLink, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-about',
  standalone: true,
  imports: [HomepageComponent, RouterLink, RouterOutlet],
  templateUrl: './about.component.html',
  styleUrl: './about.component.scss'
})
export class AboutComponent {

  companyInfo = {
    field: 'your field or industry',
    purpose: 'describe the purpose or goal of your website',
    coreValues: 'core values or principles',
    productsServices: 'describe your products or services',
    commitment: 'mention any unique aspects or qualities of your business',
    dedication: 'specific aspects of your business',
    callToAction: 'call-to-action, such as schedule a consultation, make a purchase, etc.'
  };

}

import { Routes } from '@angular/router';
import { authGuard } from './core/guards/auth.guard';

export const routes: Routes = [
  {
    path: 'login',
    loadComponent: () => import('./features/login/login').then(m => m.LoginComponent)
  },
  {
    path: 'home',
    loadComponent: () => import('./features/home/home').then(m => m.HomeComponent),
    canActivate: [authGuard],
    children: [
      {
        path: 'products',
        loadComponent: () => import('./features/products/products').then(m => m.ProductsComponent)
      },
      {
        path: 'families',
        loadComponent: () => import('./features/families/families').then(m => m.FamiliesComponent)
      },
      {
        path: 'therapeutic-groups',
        loadComponent: () => import('./features/therapeutic-groups/therapeutic-groups').then(m => m.TherapeuticGroupsComponent)
      },
      {
        path: 'laboratories',
        loadComponent: () => import('./features/laboratories/laboratories').then(m => m.LaboratoriesComponent)
      },
      {
        path: 'pharmaceutical-forms',
        loadComponent: () => import('./features/pharmaceutical-forms/pharmaceutical-forms').then(m => m.PharmaceuticalFormsComponent)
      },
      {
        path: 'posologies',
        loadComponent: () => import('./features/posologies/posologies').then(m => m.PosologiesComponent)
      },
      {
        path: '',
        redirectTo: 'products',
        pathMatch: 'full'
      }
    ]
  },
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  },
  {
    path: '**',
    redirectTo: 'home'
  }
];

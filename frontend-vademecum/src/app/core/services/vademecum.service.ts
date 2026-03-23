import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, map } from 'rxjs';
import { environment } from '../../../environments/environment';
import { ApiResponse } from '../models/api-response.model';
import { Product, Family, TherapeuticGroup, Laboratory, PharmaceuticalForm, Posology } from '../models/vademecum.model';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class VademecumService {
  private http = inject(HttpClient);
  private authService = inject(AuthService);
  private readonly apiUrl = environment.apiUrl;

  private getHeaders(): HttpHeaders {
    const token = this.authService.getToken();
    return new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    });
  }

  // --- PRODUCTOS ---
  getProducts(): Observable<Product[]> {
    return this.http.get<ApiResponse<Product[]>>(`${this.apiUrl}/products`, { headers: this.getHeaders() })
      .pipe(map(res => res.data));
  }

  getProductById(id: number): Observable<Product> {
    return this.http.get<ApiResponse<Product>>(`${this.apiUrl}/products/${id}`, { headers: this.getHeaders() })
      .pipe(map(res => res.data));
  }

  createProduct(product: Partial<Product>): Observable<ApiResponse<Product>> {
    return this.http.post<ApiResponse<Product>>(`${this.apiUrl}/products`, product, { headers: this.getHeaders() });
  }

  updateProduct(id: number, product: Partial<Product>): Observable<ApiResponse<Product>> {
    return this.http.put<ApiResponse<Product>>(`${this.apiUrl}/products/${id}`, product, { headers: this.getHeaders() });
  }

  deleteProduct(id: number): Observable<ApiResponse<null>> {
    return this.http.delete<ApiResponse<null>>(`${this.apiUrl}/products/${id}`, { headers: this.getHeaders() });
  }

  // --- FAMILIAS ---
  getFamilies(): Observable<Family[]> {
    return this.http.get<ApiResponse<Family[]>>(`${this.apiUrl}/families`, { headers: this.getHeaders() })
      .pipe(map(res => res.data));
  }

  createFamily(family: Partial<Family>): Observable<ApiResponse<Family>> {
    return this.http.post<ApiResponse<Family>>(`${this.apiUrl}/families`, family, { headers: this.getHeaders() });
  }

  updateFamily(id: number, family: Partial<Family>): Observable<ApiResponse<Family>> {
    return this.http.put<ApiResponse<Family>>(`${this.apiUrl}/families/${id}`, family, { headers: this.getHeaders() });
  }

  deleteFamily(id: number): Observable<ApiResponse<null>> {
    return this.http.delete<ApiResponse<null>>(`${this.apiUrl}/families/${id}`, { headers: this.getHeaders() });
  }

  // --- GRUPOS TERAPÉUTICOS ---
  getTherapeuticGroups(): Observable<TherapeuticGroup[]> {
    return this.http.get<ApiResponse<TherapeuticGroup[]>>(`${this.apiUrl}/therapeutic-groups`, { headers: this.getHeaders() })
      .pipe(map(res => res.data));
  }

  createTherapeuticGroup(group: Partial<TherapeuticGroup>): Observable<ApiResponse<TherapeuticGroup>> {
    return this.http.post<ApiResponse<TherapeuticGroup>>(`${this.apiUrl}/therapeutic-groups`, group, { headers: this.getHeaders() });
  }

  updateTherapeuticGroup(id: number, group: Partial<TherapeuticGroup>): Observable<ApiResponse<TherapeuticGroup>> {
    return this.http.put<ApiResponse<TherapeuticGroup>>(`${this.apiUrl}/therapeutic-groups/${id}`, group, { headers: this.getHeaders() });
  }

  deleteTherapeuticGroup(id: number): Observable<ApiResponse<null>> {
    return this.http.delete<ApiResponse<null>>(`${this.apiUrl}/therapeutic-groups/${id}`, { headers: this.getHeaders() });
  }

  // --- LABORATORIOS ---
  getLaboratories(): Observable<Laboratory[]> {
    return this.http.get<ApiResponse<Laboratory[]>>(`${this.apiUrl}/laboratories`, { headers: this.getHeaders() })
      .pipe(map(res => res.data));
  }

  createLaboratory(lab: Partial<Laboratory>): Observable<ApiResponse<Laboratory>> {
    return this.http.post<ApiResponse<Laboratory>>(`${this.apiUrl}/laboratories`, lab, { headers: this.getHeaders() });
  }

  updateLaboratory(id: number, lab: Partial<Laboratory>): Observable<ApiResponse<Laboratory>> {
    return this.http.put<ApiResponse<Laboratory>>(`${this.apiUrl}/laboratories/${id}`, lab, { headers: this.getHeaders() });
  }

  deleteLaboratory(id: number): Observable<ApiResponse<null>> {
    return this.http.delete<ApiResponse<null>>(`${this.apiUrl}/laboratories/${id}`, { headers: this.getHeaders() });
  }

  // --- FORMAS FARMACÉUTICAS ---
  getPharmaceuticalForms(): Observable<PharmaceuticalForm[]> {
    return this.http.get<ApiResponse<PharmaceuticalForm[]>>(`${this.apiUrl}/pharmaceutical-forms`, { headers: this.getHeaders() })
      .pipe(map(res => res.data));
  }

  createPharmaceuticalForm(form: Partial<PharmaceuticalForm>): Observable<ApiResponse<PharmaceuticalForm>> {
    return this.http.post<ApiResponse<PharmaceuticalForm>>(`${this.apiUrl}/pharmaceutical-forms`, form, { headers: this.getHeaders() });
  }

  updatePharmaceuticalForm(id: number, form: Partial<PharmaceuticalForm>): Observable<ApiResponse<PharmaceuticalForm>> {
    return this.http.put<ApiResponse<PharmaceuticalForm>>(`${this.apiUrl}/pharmaceutical-forms/${id}`, form, { headers: this.getHeaders() });
  }

  deletePharmaceuticalForm(id: number): Observable<ApiResponse<null>> {
    return this.http.delete<ApiResponse<null>>(`${this.apiUrl}/pharmaceutical-forms/${id}`, { headers: this.getHeaders() });
  }

  // --- POSOLOGÍAS ---
  getPosologies(): Observable<Posology[]> {
    return this.http.get<ApiResponse<Posology[]>>(`${this.apiUrl}/posologies`, { headers: this.getHeaders() })
      .pipe(map(res => res.data));
  }

  createPosology(posology: Partial<Posology>): Observable<ApiResponse<Posology>> {
    return this.http.post<ApiResponse<Posology>>(`${this.apiUrl}/posologies`, posology, { headers: this.getHeaders() });
  }

  updatePosology(id: number, posology: Partial<Posology>): Observable<ApiResponse<Posology>> {
    return this.http.put<ApiResponse<Posology>>(`${this.apiUrl}/posologies/${id}`, posology, { headers: this.getHeaders() });
  }

  deletePosology(id: number): Observable<ApiResponse<null>> {
    return this.http.delete<ApiResponse<null>>(`${this.apiUrl}/posologies/${id}`, { headers: this.getHeaders() });
  }
}

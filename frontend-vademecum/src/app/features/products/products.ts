import { Component, inject, signal, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { VademecumService } from '../../core/services/vademecum.service';
import { Product, Family, Laboratory, PharmaceuticalForm, Posology } from '../../core/models/vademecum.model';

@Component({
  selector: 'app-products',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './products.html',
  styleUrls: ['./products.css']
})
export class ProductsComponent implements OnInit {
  private vademecumService = inject(VademecumService);

  products = signal<Product[]>([]);
  families = signal<Family[]>([]);
  laboratories = signal<Laboratory[]>([]);
  pharmaForms = signal<PharmaceuticalForm[]>([]);
  posologies = signal<Posology[]>([]);
  
  isLoading = signal(false);
  isModalOpen = signal(false);
  isEditing = signal(false);

  // Form Model
  currentProduct: Partial<Product> = this.getEmptyProduct();

  ngOnInit(): void {
    this.loadData();
  }

  getEmptyProduct(): Partial<Product> {
    return {
      commercial_name: '',
      generic_name: '',
      id_family: undefined,
      id_laboratory: undefined,
      id_pharmaceutical_form: undefined,
      id_posology: undefined,
      concentration: '',
      action_mechanism: '',
      notes: '',
      is_active: true
    };
  }

  loadData(): void {
    this.isLoading.set(true);
    // Carga paralela simplificada
    this.vademecumService.getProducts().subscribe(data => this.products.set(data));
    this.vademecumService.getFamilies().subscribe(data => this.families.set(data));
    this.vademecumService.getLaboratories().subscribe(data => this.laboratories.set(data));
    this.vademecumService.getPharmaceuticalForms().subscribe(data => this.pharmaForms.set(data));
    this.vademecumService.getPosologies().subscribe(data => {
      this.posologies.set(data);
      this.isLoading.set(false);
    });
  }

  openCreateModal() {
    this.isEditing.set(false);
    this.currentProduct = this.getEmptyProduct();
    this.isModalOpen.set(true);
  }

  openEditModal(product: Product) {
    this.isEditing.set(true);
    this.currentProduct = { ...product };
    this.isModalOpen.set(true);
  }

  closeModal() {
    this.isModalOpen.set(false);
  }

  saveProduct() {
    if (this.isEditing()) {
      this.vademecumService.updateProduct(this.currentProduct.id_product!, this.currentProduct).subscribe(() => {
        this.loadData();
        this.closeModal();
      });
    } else {
      this.vademecumService.createProduct(this.currentProduct).subscribe(() => {
        this.loadData();
        this.closeModal();
      });
    }
  }

  deleteProduct(id: number) {
    if (confirm('¿Estás seguro de eliminar este producto?')) {
      this.vademecumService.deleteProduct(id).subscribe(() => {
        this.loadData();
      });
    }
  }

  getFamilyName(id?: number) {
    return this.families().find(f => f.id_family === id)?.name || 'N/A';
  }
}

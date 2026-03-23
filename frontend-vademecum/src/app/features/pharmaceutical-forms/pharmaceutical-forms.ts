import { Component, inject, signal, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { VademecumService } from '../../core/services/vademecum.service';
import { PharmaceuticalForm } from '../../core/models/vademecum.model';

@Component({
  selector: 'app-pharmaceutical-forms',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './pharmaceutical-forms.html',
  styleUrls: ['./pharmaceutical-forms.css']
})
export class PharmaceuticalFormsComponent implements OnInit {
  private vademecumService = inject(VademecumService);

  forms = signal<PharmaceuticalForm[]>([]);
  isLoading = signal(false);
  isModalOpen = signal(false);
  isEditing = signal(false);

  currentForm: Partial<PharmaceuticalForm> = { name: '' };

  ngOnInit(): void {
    this.loadData();
  }

  loadData(): void {
    this.isLoading.set(true);
    this.vademecumService.getPharmaceuticalForms().subscribe(data => {
      this.forms.set(data);
      this.isLoading.set(false);
    });
  }

  openCreateModal() {
    this.isEditing.set(false);
    this.currentForm = { name: '' };
    this.isModalOpen.set(true);
  }

  openEditModal(form: PharmaceuticalForm) {
    this.isEditing.set(true);
    this.currentForm = { ...form };
    this.isModalOpen.set(true);
  }

  closeModal() {
    this.isModalOpen.set(false);
  }

  saveForm() {
    if (this.isEditing()) {
      this.vademecumService.updatePharmaceuticalForm(this.currentForm.id_pharmaceutical_form!, this.currentForm).subscribe(() => {
        this.loadData();
        this.closeModal();
      });
    } else {
      this.vademecumService.createPharmaceuticalForm(this.currentForm).subscribe(() => {
        this.loadData();
        this.closeModal();
      });
    }
  }

  deleteForm(id: number) {
    if (confirm('¿Estás seguro de eliminar esta forma farmacéutica?')) {
      this.vademecumService.deletePharmaceuticalForm(id).subscribe(() => {
        this.loadData();
      });
    }
  }
}

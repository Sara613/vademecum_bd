import { Component, inject, signal, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { VademecumService } from '../../core/services/vademecum.service';
import { Laboratory } from '../../core/models/vademecum.model';

@Component({
  selector: 'app-laboratories',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './laboratories.html',
  styleUrls: ['./laboratories.css']
})
export class LaboratoriesComponent implements OnInit {
  private vademecumService = inject(VademecumService);

  laboratories = signal<Laboratory[]>([]);
  isLoading = signal(false);
  isModalOpen = signal(false);
  isEditing = signal(false);

  currentLab: Partial<Laboratory> = { name: '' };

  ngOnInit(): void {
    this.loadData();
  }

  loadData(): void {
    this.isLoading.set(true);
    this.vademecumService.getLaboratories().subscribe(data => {
      this.laboratories.set(data);
      this.isLoading.set(false);
    });
  }

  openCreateModal() {
    this.isEditing.set(false);
    this.currentLab = { name: '' };
    this.isModalOpen.set(true);
  }

  openEditModal(lab: Laboratory) {
    this.isEditing.set(true);
    this.currentLab = { ...lab };
    this.isModalOpen.set(true);
  }

  closeModal() {
    this.isModalOpen.set(false);
  }

  saveLab() {
    if (this.isEditing()) {
      this.vademecumService.updateLaboratory(this.currentLab.id_laboratory!, this.currentLab).subscribe(() => {
        this.loadData();
        this.closeModal();
      });
    } else {
      this.vademecumService.createLaboratory(this.currentLab).subscribe(() => {
        this.loadData();
        this.closeModal();
      });
    }
  }

  deleteLab(id: number) {
    if (confirm('¿Estás seguro de eliminar este laboratorio?')) {
      this.vademecumService.deleteLaboratory(id).subscribe(() => {
        this.loadData();
      });
    }
  }
}

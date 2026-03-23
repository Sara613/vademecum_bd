import { Component, inject, signal, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { VademecumService } from '../../core/services/vademecum.service';
import { Posology } from '../../core/models/vademecum.model';

@Component({
  selector: 'app-posologies',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './posologies.html',
  styleUrls: ['./posologies.css']
})
export class PosologiesComponent implements OnInit {
  private vademecumService = inject(VademecumService);

  posologies = signal<Posology[]>([]);
  isLoading = signal(false);
  isModalOpen = signal(false);
  isEditing = signal(false);

  currentPosology: Partial<Posology> = { name: '' };

  ngOnInit(): void {
    this.loadData();
  }

  loadData(): void {
    this.isLoading.set(true);
    this.vademecumService.getPosologies().subscribe(data => {
      this.posologies.set(data);
      this.isLoading.set(false);
    });
  }

  openCreateModal() {
    this.isEditing.set(false);
    this.currentPosology = { name: '' };
    this.isModalOpen.set(true);
  }

  openEditModal(posology: Posology) {
    this.isEditing.set(true);
    this.currentPosology = { ...posology };
    this.isModalOpen.set(true);
  }

  closeModal() {
    this.isModalOpen.set(false);
  }

  savePosology() {
    if (this.isEditing()) {
      this.vademecumService.updatePosology(this.currentPosology.id_posology!, this.currentPosology).subscribe(() => {
        this.loadData();
        this.closeModal();
      });
    } else {
      this.vademecumService.createPosology(this.currentPosology).subscribe(() => {
        this.loadData();
        this.closeModal();
      });
    }
  }

  deletePosology(id: number) {
    if (confirm('¿Estás seguro de eliminar esta posología?')) {
      this.vademecumService.deletePosology(id).subscribe(() => {
        this.loadData();
      });
    }
  }
}

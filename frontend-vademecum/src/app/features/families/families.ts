import { Component, inject, signal, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { VademecumService } from '../../core/services/vademecum.service';
import { Family, TherapeuticGroup } from '../../core/models/vademecum.model';

@Component({
  selector: 'app-families',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './families.html',
  styleUrls: ['./families.css']
})
export class FamiliesComponent implements OnInit {
  private vademecumService = inject(VademecumService);

  families = signal<Family[]>([]);
  therapeuticGroups = signal<TherapeuticGroup[]>([]);
  
  isLoading = signal(false);
  isModalOpen = signal(false);
  isEditing = signal(false);

  currentFamily: Partial<Family> = this.getEmptyFamily();

  ngOnInit(): void {
    this.loadData();
  }

  getEmptyFamily(): Partial<Family> {
    return {
      name: '',
      potential_illness: '',
      id_therapeutic_group: undefined
    };
  }

  loadData(): void {
    this.isLoading.set(true);
    this.vademecumService.getFamilies().subscribe(data => this.families.set(data));
    this.vademecumService.getTherapeuticGroups().subscribe(data => {
      this.therapeuticGroups.set(data);
      this.isLoading.set(false);
    });
  }

  openCreateModal() {
    this.isEditing.set(false);
    this.currentFamily = this.getEmptyFamily();
    this.isModalOpen.set(true);
  }

  openEditModal(family: Family) {
    this.isEditing.set(true);
    this.currentFamily = { ...family };
    this.isModalOpen.set(true);
  }

  closeModal() {
    this.isModalOpen.set(false);
  }

  saveFamily() {
    if (this.isEditing()) {
      this.vademecumService.updateFamily(this.currentFamily.id_family!, this.currentFamily).subscribe(() => {
        this.loadData();
        this.closeModal();
      });
    } else {
      this.vademecumService.createFamily(this.currentFamily).subscribe(() => {
        this.loadData();
        this.closeModal();
      });
    }
  }

  deleteFamily(id: number) {
    if (confirm('¿Estás seguro de eliminar esta familia?')) {
      this.vademecumService.deleteFamily(id).subscribe(() => {
        this.loadData();
      });
    }
  }

  getTherapeuticGroupName(id?: number) {
    return this.therapeuticGroups().find(g => g.id_therapeutic_group === id)?.name || 'N/A';
  }
}

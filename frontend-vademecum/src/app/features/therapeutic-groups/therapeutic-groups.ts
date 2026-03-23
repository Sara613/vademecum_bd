import { Component, inject, signal, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { VademecumService } from '../../core/services/vademecum.service';
import { TherapeuticGroup } from '../../core/models/vademecum.model';

@Component({
  selector: 'app-therapeutic-groups',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './therapeutic-groups.html',
  styleUrls: ['./therapeutic-groups.css']
})
export class TherapeuticGroupsComponent implements OnInit {
  private vademecumService = inject(VademecumService);

  groups = signal<TherapeuticGroup[]>([]);
  isLoading = signal(false);
  isModalOpen = signal(false);
  isEditing = signal(false);

  currentGroup: Partial<TherapeuticGroup> = { name: '' };

  ngOnInit(): void {
    this.loadData();
  }

  loadData(): void {
    this.isLoading.set(true);
    this.vademecumService.getTherapeuticGroups().subscribe(data => {
      this.groups.set(data);
      this.isLoading.set(false);
    });
  }

  openCreateModal() {
    this.isEditing.set(false);
    this.currentGroup = { name: '' };
    this.isModalOpen.set(true);
  }

  openEditModal(group: TherapeuticGroup) {
    this.isEditing.set(true);
    this.currentGroup = { ...group };
    this.isModalOpen.set(true);
  }

  closeModal() {
    this.isModalOpen.set(false);
  }

  saveGroup() {
    if (this.isEditing()) {
      this.vademecumService.updateTherapeuticGroup(this.currentGroup.id_therapeutic_group!, this.currentGroup).subscribe(() => {
        this.loadData();
        this.closeModal();
      });
    } else {
      this.vademecumService.createTherapeuticGroup(this.currentGroup).subscribe(() => {
        this.loadData();
        this.closeModal();
      });
    }
  }

  deleteGroup(id: number) {
    if (confirm('¿Estás seguro de eliminar este grupo?')) {
      this.vademecumService.deleteTherapeuticGroup(id).subscribe(() => {
        this.loadData();
      });
    }
  }
}

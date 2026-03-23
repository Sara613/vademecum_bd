export interface TherapeuticGroup {
  id_therapeutic_group: number;
  name: string;
}

export interface Family {
  id_family: number;
  name: string;
  potential_illness?: string;
  id_therapeutic_group: number;
}

export interface Laboratory {
  id_laboratory: number;
  name: string;
}

export interface PharmaceuticalForm {
  id_pharmaceutical_form: number;
  name: string;
}

export interface Posology {
  id_posology: number;
  name: string;
}

export interface Product {
  id_product: number;
  commercial_name: string;
  generic_name?: string;
  id_family?: number;
  action_mechanism?: string;
  id_laboratory?: number;
  concentration?: string;
  id_pharmaceutical_form?: number;
  id_posology?: number;
  notes?: string;
  is_active: boolean;
}

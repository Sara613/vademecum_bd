export interface User {
  id: number;
  identification: string;
  full_name: string;
  is_active: boolean;
}

export interface AuthResponse {
  access_token: string;
  user: User;
}

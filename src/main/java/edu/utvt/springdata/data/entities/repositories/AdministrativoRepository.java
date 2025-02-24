package edu.utvt.springdata.data.entities.repositories;

import java.util.UUID;

import org.springframework.data.jpa.repository.JpaRepository;

import edu.utvt.springdata.data.entities.Administrativo;

public interface AdministrativoRepository extends JpaRepository<Administrativo, UUID> {
    
}

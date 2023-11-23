package com.AbbonamentiPalestra.Repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.AbbonamentiPalestra.Class.UtenteAccesso;

@Repository
public interface UtenteAccessoRepository extends CrudRepository<UtenteAccesso, Long>{

	UtenteAccesso findByUsername(String username);
	
}

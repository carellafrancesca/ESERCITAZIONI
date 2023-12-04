package com.AbbonamentiPalestra.Repository;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.AbbonamentiPalestra.Class.Recensioni;

@Repository
public interface RecensioneRepository extends CrudRepository<Recensioni, Long>{

}
